from playwright.sync_api import sync_playwright
import time
from sys import argv, exit, platform
import openai
import os
from dotenv import load_dotenv
from SwiggyCrawlerStateless import SwiggyCrawlerStateless

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
prompt_template = """
You are an agent controlling a browser. You are given:
	(1) an objective that you are trying to achieve
	(2) the URL of your current web page
	(3) a simplified text description of what's visible in the browser window (more on that below)
You can issue these commands:
WIP
The format of the browser content is highly simplified; all formatting elements are stripped.
Based on your given objective, issue whatever command you believe will get you closest to achieving your goal.
You always start on Google; you should submit a search query to Google that will take you to the best page for
achieving your objective. And then interact with that page to achieve your objective.
If you find yourself on Google and there are no search results displayed yet, you should probably issue a command 
like "TYPESUBMIT 7 "search query"" to get to a more useful page.
Then, if you find yourself on a Google search results page, you might issue the command "CLICK 24" to click
on the first link in the search results. (If your previous command was a TYPESUBMIT your next command should
probably be a CLICK.)
Don't try to interact with elements that you can't see.
Here are some examples:
EXAMPLE 1:
==================================================
CURRENT BROWSER CONTENT:
------------------
<link id=1>About</link>
<link id=2>Store</link>
<link id=3>Gmail</link>
<link id=4>Images</link>
<link id=5>(Google apps)</link>
<link id=6>Sign in</link>
<img id=7 alt="(Google)"/>
<input id=8 alt="Search"></input>
<button id=9>(Search by voice)</button>
<button id=10>(Google Search)</button>
<button id=11>(I'm Feeling Lucky)</button>
<link id=12>Advertising</link>
<link id=13>Business</link>
<link id=14>How Search works</link>
<link id=15>Carbon neutral since 2007</link>
<link id=16>Privacy</link>
<link id=17>Terms</link>
<text id=18>Settings</text>
------------------
OBJECTIVE: Find a 2 bedroom house for sale in Anchorage AK for under $750k
CURRENT URL: https://www.google.com/
YOUR COMMAND: 
TYPESUBMIT 8 "anchorage redfin"
==================================================
EXAMPLE 2:
==================================================
CURRENT BROWSER CONTENT:
------------------
<link id=1>About</link>
<link id=2>Store</link>
<link id=3>Gmail</link>
<link id=4>Images</link>
<link id=5>(Google apps)</link>
<link id=6>Sign in</link>
<img id=7 alt="(Google)"/>
<input id=8 alt="Search"></input>
<button id=9>(Search by voice)</button>
<button id=10>(Google Search)</button>
<button id=11>(I'm Feeling Lucky)</button>
<link id=12>Advertising</link>
<link id=13>Business</link>
<link id=14>How Search works</link>
<link id=15>Carbon neutral since 2007</link>
<link id=16>Privacy</link>
<link id=17>Terms</link>
<text id=18>Settings</text>
------------------
OBJECTIVE: Make a reservation for 4 at Dorsia at 8pm
CURRENT URL: https://www.google.com/
YOUR COMMAND: 
TYPESUBMIT 8 "dorsia nyc opentable"
==================================================
EXAMPLE 3:
==================================================
CURRENT BROWSER CONTENT:
------------------
<button id=1>For Businesses</button>
<button id=2>Mobile</button>
<button id=3>Help</button>
<button id=4 alt="Language Picker">EN</button>
<link id=5>OpenTable logo</link>
<button id=6 alt ="search">Search</button>
<text id=7>Find your table for any occasion</text>
<button id=8>(Date selector)</button>
<text id=9>Sep 28, 2022</text>
<text id=10>7:00 PM</text>
<text id=11>2 people</text>
<input id=12 alt="Location, Restaurant, or Cuisine"></input> 
<button id=13>Let’s go</button>
<text id=14>It looks like you're in Peninsula. Not correct?</text> 
<button id=15>Get current location</button>
<button id=16>Next</button>
------------------
OBJECTIVE: Make a reservation for 4 for dinner at Dorsia in New York City at 8pm
CURRENT URL: https://www.opentable.com/
YOUR COMMAND: 
TYPESUBMIT 12 "dorsia new york city"
==================================================
The current browser content, objective, and current URL follow. Reply with your next command to the browser.
CURRENT BROWSER CONTENT:
------------------
$browser_content
------------------
OBJECTIVE: $objective
CURRENT URL: $url
PREVIOUS COMMAND: $previous_command
YOUR COMMAND:
"""

if (
	__name__ == "__main__"
):
	_crawler = SwiggyCrawlerStateless()
	openai.api_key = os.environ.get("OPENAI_API_KEY")

	def print_help():
		print(
			"WIP",
		)

	def get_gpt_command(prompt):
		response = openai.Completion.create(model="text-davinci-002", prompt=prompt, temperature=0.5, best_of=10, n=3, max_tokens=50)
		return response.choices[0].text

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
				search_elements = _crawler.search_directly(str_search)
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

	objective = "Order margherita pizza from dominos"
	print("\nWelcome to swiggy bot! What can I do for you today?")
	i = input()
	if len(i) > 0:
		objective = i

	observation = 'Search Bar'
	done = False
	state_stack = [(PageState.SEARCH_MAIN, None, observation)]

	running_context = f'Instruction: {objective}\nObservation: {observation}\nAction: '

	# go to the swiggy main page
	_crawler.reset()
	klk = 0
	try:
		while True:
			print(f'Attempt {klk}')
			print(running_context)

			gpt_cmd = "" # get_gpt_command(running_context)
			gpt_cmd = gpt_cmd.strip()

			if len(gpt_cmd) > 0:
				print("Suggested command: " + gpt_cmd)

			command = input()
			command = command.strip()
			if command == "":
				_, observation, done = step(state_stack, gpt_cmd)
				running_context += f"{gpt_cmd}\nObservation: {observation}\nAction: "
			elif command == "help":
				print_help()
			elif command == "context":
				print(f"{running_context}")
			else:
				_, observation, done = step(state_stack, command)
				# append to running context
				running_context += f"{command}\nObservation: {observation}\nAction: "
				
			if done:
				print(f"Exiting ...")
				break
			
			# TODO: 
			# running context needs to be saved after this for example

	except KeyboardInterrupt:
		print("\n[!] Ctrl+C detected, exiting gracefully.")
		exit(0)
