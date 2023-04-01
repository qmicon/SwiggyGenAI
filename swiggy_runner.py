from playwright.sync_api import sync_playwright
import time
from sys import argv, exit, platform
import openai
import os
from dotenv import load_dotenv
from SwiggyCrawlerStateless import SwiggyCrawlerStateless
import random


load_dotenv()

from enum import Enum
class PageState(Enum):
	SEARCH_MAIN = 0
	SEARCH_SUGGESTIONS = 1
	SEARCH_RESTAURANTS = 2
	MENU_OPTIONS = 3
	CHECKOUT = 4

quiet = False
if len(argv) >= 2:
	if argv[1] == '-q' or argv[1] == '--quiet':
		quiet = True
		print(
			"Running in quiet mode (HTML and other content hidden); \n"
			+ "exercise caution when running suggested commands."
		)

# TODO: Update the prompt template with ReAct examples of trajectories.
prompt_template = f"""
You are an agent for swiggy.com, a food ordering web app. You are given an instruction about the order you need to fulfill

You can issue these commands:
(1) SEARCH <restaurant_name> - to find restaurants with restaurant_name on swiggy's website
(2) CLICK x - to open the menu of restaurant with id:x from search results
(3) ADD x,y - to add y quantity of item with id:x from menu to the shopping cart
(4) CHECKOUT - when you are done with adding items and want to place the order 

You mainly see 3 kind of pages in the app:
(1) Search Bar page - this is where you start your journey
(2) Search Results page - this is where you see the restaurant search results
(3) Menu page - this is where you see the menu when you click on restaurant

You can only Think and Act. Do not try to print out the observation for search or menu options. Don't try to interact with elements that you can't see.
Here are some examples:
===========
EXAMPLE 1:
{open("../trajectory_3.txt", "r").read()}
===========
REAL:
Now understand the customer's instruction. Make sure to carefully observe and think before you act.
"""
def print_help():
		return "WIP"

def get_gpt_command(template, context):
	prompt = template + '\n' + context
	response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=0.5, best_of=10, n=3, max_tokens=50)
	return response.choices[0].text.strip().split('\n')[0]

def step(state_stack, cmd, crawler = None):
	if crawler:
		_crawler = crawler
	done = False
	new_state = state_stack[-1]
	observation = None
	cmd = cmd.split("\n")[0]
	bot_response = cmd

	if cmd.startswith("RESET"):
		# Usage like RESET
		_crawler.reset()
		observation = "Search Bar"
		state_stack = [] # empty the stack for states
		new_state = (PageState.SEARCH_MAIN, None, observation)
		state_stack.append(new_state)
	
	elif cmd.startswith("SEARCH"):
		# usage like SEARCH string
		str_search = cmd.strip().split("SEARCH")[1].strip()
		category = "Restaurant"
		try:
			search_suggest_elements = _crawler.search_suggest(str_search)
			search_elements = _crawler.search(search_suggest_elements, str_search, category)
			observation = f"Search results for {str_search}" + _crawler.render_search_restaurants(search_elements)
			new_state = (PageState.SEARCH_RESTAURANTS, search_elements, observation)
			state_stack.append(new_state)
			bot_response = f"Searched results for {str_search}"
		except:
			search_elements = _crawler.search_directly("")
			observation = f"Search results for {str_search}" + _crawler.render_search_restaurants(search_elements)
			new_state = (PageState.SEARCH_RESTAURANTS, search_elements, observation)
			state_stack.append(new_state)
			bot_response = f"Searched results for {str_search}"

	elif cmd.startswith("BACK"):
		# usage like BACK
		# go to the previous page, this just means we will pop the stack and return it
		new_state = state_stack.pop(-1) # is a tuple of (state_type, obs)
		new_state = state_stack[-1]
		observation = new_state[-1]

	elif cmd.startswith("CLICK"):
		# usage like CLICK 4
		commasplit = cmd.split(",")
		id = commasplit[0].split(" ")[1]
		# see if this is valid action, click is only permitted in search pages
		try:
			id = int(id)
			curr_state = state_stack[-1]
			if curr_state[0] == PageState.SEARCH_RESTAURANTS:
				# permitted
				restaurant_elements = curr_state[1]
				# chosen restaurant
				retaurant_info = _crawler.parse_search_restaurant(restaurant_elements[id])
				# menu for chosen restaurant
				menu_elements = _crawler.search_restaurant_by_index(restaurant_elements, id)
				observation = f"Menu page for {retaurant_info['Restaurant name'].strip()}" + _crawler.render_menu_items(menu_elements)
				# create new state
				new_state = (PageState.MENU_OPTIONS, menu_elements, observation)
				state_stack.append(new_state)
				bot_response = f"Opened menu page for {retaurant_info['Restaurant name'].strip()}"
			else:
				# action is not permitted
				observation = f"Invalid action! We are not on the restaurant search page." #Current page is {prev_obs}
				# no update to state
		except Exception as e:
			observation = f"Invalid action! id needs to be integer." # Current page is {prev_obs}
	
	elif cmd.startswith("ADD"):
		# Usage like ADD 123,2
		commasplit = cmd.strip().split()[1].split(',')
		id, qty = commasplit
		# see if this is valid action, click is only permitted in search pages
		try:
			id = int(id)
			qty = int(qty)
			curr_state = state_stack[-1]
			if curr_state[0] == PageState.MENU_OPTIONS:
				# permitted
				menu_elements = curr_state[1]
				_crawler.add_menu_item_by_index_x_times(menu_elements, id, qty)

				observation = f"Added {qty} of item {id} to cart"
				name = _crawler.parse_menu_element(menu_elements[id]).split(".")[1].strip()
				bot_response = f"Added {qty} {name}"
			else:
				# action is not permitted
				observation = f"Invalid action! We are not on the restaurant menu page." # Current page is {prev_obs}
				# no update to state
		except Exception as e:
			observation = f"Invalid action! Both id and qty needs to be integer." #  Current page is {prev_obs}

	elif cmd.startswith("CHECKOUT"):
		# Usage like CHECKOUT
		_crawler.checkout()
		observation = "Order placed!"
		new_state = (PageState.CHECKOUT, None, observation)
		state_stack.append(new_state)
		done = True
		bot_response = observation
	elif cmd.startswith("THINK"):
		# Usage like THINK If I want to do stuff, etc.. 
		observation = "OK"
		new_state = state_stack[-1]
	else:
		observation = "Invalid action!"
		new_state = state_stack[-1]

	time.sleep(1)
	return new_state, observation, done, state_stack, bot_response


if (
	__name__ == "__main__"
):
	_crawler = SwiggyCrawlerStateless()
	openai.api_key = os.environ.get("OPENAI_API_KEY")

	def print_help():
		print(
			"WIP",
		)

	def step(state_stack, cmd):
		done = False
		new_state = state_stack[-1]
		observation = None
		cmd = cmd.split("\n")[0]

		if cmd.startswith("RESET"):
			# Usage like RESET
			_crawler.reset()
			observation = "Search Bar"
			state_stack = [] # empty the stack for states
			new_state = (PageState.SEARCH_MAIN, None, observation)
			state_stack.append(new_state)
		
		elif cmd.startswith("SEARCH"):
			# usage like SEARCH string
			str_search = cmd.strip().split("SEARCH")[1].strip()
			category = "Restaurant"
			try:
				search_suggest_elements = _crawler.search_suggest(str_search)
				search_elements = _crawler.search(search_suggest_elements, str_search, category)
				observation = f"Search results for {str_search}" + _crawler.render_search_restaurants(search_elements)
				new_state = (PageState.SEARCH_RESTAURANTS, search_elements, observation)
				state_stack.append(new_state)
			except:
				search_elements = _crawler.search_directly("")
				observation = f"Search results for {str_search}" + _crawler.render_search_restaurants(search_elements)
				new_state = (PageState.SEARCH_RESTAURANTS, search_elements, observation)
				state_stack.append(new_state)

		elif cmd.startswith("BACK"):
			# usage like BACK
			# go to the previous page, this just means we will pop the stack and return it
			new_state = state_stack.pop(-1) # is a tuple of (state_type, obs)
			new_state = state_stack[-1]
			observation = new_state[-1]

		elif cmd.startswith("CLICK"):
			# usage like CLICK 4
			commasplit = cmd.split(",")
			id = commasplit[0].split(" ")[1]
			# see if this is valid action, click is only permitted in search pages
			try:
				id = int(id)
				curr_state = state_stack[-1]
				if curr_state[0] == PageState.SEARCH_RESTAURANTS:
					# permitted
					restaurant_elements = curr_state[1]
					# chosen restaurant
					retaurant_info = _crawler.parse_search_restaurant(restaurant_elements[id])
					# menu for chosen restaurant
					menu_elements = _crawler.search_restaurant_by_index(restaurant_elements, id)
					observation = f"Menu page for {retaurant_info['Restaurant name'].strip()}" + _crawler.render_menu_items(menu_elements)
					# create new state
					new_state = (PageState.MENU_OPTIONS, menu_elements, observation)
					state_stack.append(new_state)
				else:
					# action is not permitted
					observation = f"Invalid action! We are not on the restaurant search page." #Current page is {prev_obs}
					# no update to state
			except Exception as e:
				observation = f"Invalid action! id needs to be integer." # Current page is {prev_obs}
		
		elif cmd.startswith("ADD"):
			# Usage like ADD 123,2
			commasplit = cmd.strip().split()[1].split(',')
			id, qty = commasplit
			# see if this is valid action, click is only permitted in search pages
			try:
				id = int(id)
				qty = int(qty)
				curr_state = state_stack[-1]
				if curr_state[0] == PageState.MENU_OPTIONS:
					# permitted
					menu_elements = curr_state[1]
					_crawler.add_menu_item_by_index_x_times(menu_elements, id, qty)

					observation = f"Added {qty} of item {id} to cart"
				else:
					# action is not permitted
					observation = f"Invalid action! We are not on the restaurant menu page." # Current page is {prev_obs}
					# no update to state
			except Exception as e:
				observation = f"Invalid action! Both id and qty needs to be integer." #  Current page is {prev_obs}

		elif cmd.startswith("CHECKOUT"):
			# Usage like CHECKOUT
			observation = "Order placed!"
			new_state = (PageState.CHECKOUT, None, observation)
			state_stack.append(new_state)
			done = True
		elif cmd.startswith("THINK"):
			# Usage like THINK If I want to do stuff, etc.. 
			observation = "OK"
			new_state = state_stack[-1]
		else:
			observation = "Invalid action!"
			new_state = state_stack[-1]

		time.sleep(1)
		return new_state, observation, done

	objective = "Order big grilled chicken from burger king"
	print("\nWelcome to swiggy bot! What can I do for you today?")
	i = input()
	if len(i) > 0:
		objective = i
	
	observation = 'Search Bar'
	done = False
	state_stack = [(PageState.SEARCH_MAIN, None, observation)]
	
	# if klk is even, we think, if klk is odd, we act
	klk = 0
	running_context = f'Instruction: {objective}\nObservation: {observation}'

	# go to the swiggy main page
	_crawler.reset()
	try:
		while True:
			
			if klk % 2 == 0:
				running_context += '\nThought: '
			else:
				running_context += '\nAction: '

			print(f'\nIteration {klk}')
			print(running_context)

			gpt_cmd = get_gpt_command(prompt_template, running_context)
			gpt_cmd = gpt_cmd.strip()

			if len(gpt_cmd) > 0:
				print("Suggested command: " + gpt_cmd)

			command = input()
			command = command.strip()
			if command == "":
				if klk % 2 != 0:
					# now act
					_, observation, done = step(state_stack, gpt_cmd)
					running_context += f"{gpt_cmd}\nObservation: {observation}"
				else:
					# only think
					running_context += f"{gpt_cmd}"

			elif command == "help":
				print_help()
			elif command == "context":
				print(f"{running_context}")
			else:
				if klk % 2 != 0:
					_, observation, done = step(state_stack, command)
					# append to running context
					running_context += f"{command}\nObservation: {observation}"
				else:
					# only think
					running_context += f"{command}"
				
			if done:
				print(f"Exiting ...")
				hash = random.getrandbits(16)
				with open(f"{hash}.txt", 'w') as fp:
					fp.write(running_context)
				break
			
			klk += 1
			# TODO: 
			# running context needs to be saved after this for example

	except KeyboardInterrupt:
		print("\n[!] Ctrl+C detected, exiting gracefully.")
		exit(0)
