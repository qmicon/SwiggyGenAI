import os
from flask import Flask, render_template, request, jsonify
import sys
from gevent import monkey
monkey.patch_all()

sys.path.append('..')

from SwiggyCrawlerStateless import SwiggyCrawlerStateless
from swiggy_runner import step, print_help, PageState

app = Flask(__name__)
crawler = SwiggyCrawlerStateless()
gpt_cmd = "Bot Response"
observation = 'Search Bar'
done = False
state_stack = [(PageState.SEARCH_MAIN, None, observation)]
running_context = f'Instruction: {gpt_cmd}\nObservation: {observation}\nAction: '

@app.route("/")
def hello():
    return render_template('chat.html')

@app.route("/ask", methods=['POST'])
def ask():
    global state_stack, running_context, done,gpt_cmd,observation, crawler
    message = str(request.form['messageText'])

    while True:

        if message == "":
             _, observation, done, state_stack = step(state_stack, gpt_cmd, crawler)
             cmd = f"{gpt_cmd}\nObservation: {observation}\nAction: "
             running_context += cmd
             return_val = {'status':'OK','answer':cmd}

        elif message == "help":
            return_val = {'status':'OK','answer': print_help()}
        elif message == "context":
            return_val = {'status':'OK','answer': running_context}
        else:
            _, observation, done, state_stack = step(state_stack, message, crawler)
            # append to running context
            cmd = f"{message}\nObservation: {observation}\nAction: "
            running_context += cmd
            return_val = {'status':'OK','answer':cmd}
				
        if done:
            if return_val:
                return_val['answer'] += "\nDone"

        return jsonify(return_val)
            

if __name__ == "__main__":
    app.run()