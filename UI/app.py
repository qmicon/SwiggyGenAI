import os
from flask import Flask, render_template, request, jsonify
import sys
from gevent import monkey
from dotenv import load_dotenv
import time

monkey.patch_all()
load_dotenv()
sys.path.append('..')

from SwiggyCrawlerStateless import SwiggyCrawlerStateless
from swiggy_runner import step, print_help, PageState, prompt_template, get_gpt_command

app = Flask(__name__)
crawler = SwiggyCrawlerStateless()
objective = ''
observation = 'Search Bar'
done = False
state_stack = [(PageState.SEARCH_MAIN, None, observation)]
running_context = f'Instruction: {objective}\nObservation: {observation}'

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    global state_stack, running_context, done,gpt_cmd,observation, crawler
    message = str(request.form['messageText'])

    while True:

        if done:
            crawler.reset()
            return_val = {'status':'OK','answer':"What do you want to order next?"}
            done = False
        elif message == "":
            running_context += '\nAction: '
            gpt_cmd = get_gpt_command(prompt_template, running_context)
            gpt_cmd = gpt_cmd.strip()
            _, observation, done, state_stack, bot_res = step(state_stack, gpt_cmd, crawler)
            running_context += f"{gpt_cmd}\nObservation: {observation}"
            return_val = {'status':'OK','answer':bot_res}

        elif message == "help":
            return_val = {'status':'OK','answer': print_help()}
        elif message == "context":
            return_val = {'status':'OK','answer': running_context}
        else:
            objective = message
            observation = 'Search Bar'
            done = False
            state_stack = [(PageState.SEARCH_MAIN, None, observation)]
            running_context = f'Instruction: {objective}\nObservation: {observation}'
            running_context += '\nAction: '
            gpt_cmd = get_gpt_command(prompt_template, running_context)
            gpt_cmd = gpt_cmd.strip()
            _, observation, done, state_stack, bot_res = step(state_stack, gpt_cmd, crawler)
            running_context += f"{gpt_cmd}\nObservation: {observation}"
            return_val = {'status':'OK','answer':bot_res}
				
        print(running_context)
        return jsonify(return_val)
            

if __name__ == "__main__":
    app.run()