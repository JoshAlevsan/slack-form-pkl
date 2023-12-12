#   ========================
#   || Library Imports    ||
#   ========================

# import json
from dotenv import dotenv_values
from flask import Flask, request, render_template
from flaskext.mysql import MySQL
#   from flask_mysqldb import MySQL
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from app.form_template import FormTemplate
from app.form_submission import FormSubmission



#   ========================
#   || Config Loading     ||
#   ========================
config = dotenv_values(".form_env")



#   ========================
#   || App Initialization ||
#   ========================

current_form = None
app = Flask(__name__)
slack = App(
    token = config["SLACK_BOT_TOKEN"],
    signing_secret = config["SLACK_SIGNING_SECRET"]
)
slack_handler = SlackRequestHandler(slack)



#   ========================
#   || Route Section      ||
#   ========================

#   -- Connection check. --
@app.route('/', methods = ['GET'])
def slash_root():
    return render_template("conn_response.html")

#   -- Form view call route. --
@app.route('/slack-api/form', methods = ['POST'])
def slack_form():
    response = slack_handler.handle(request)
    return response

#   -- Form submit post route --
@app.route('/slack-api/action', methods = ['POST'])
def slack_action():
    response = slack_handler.handle(request)
    return response



#   ========================
#   || Event Section      ||
#   ========================
 
#   -- Form Initialize Event --
@slack.command("/form")
def init(ack, body, client):
    ack()

    global current_form
    current_form = FormTemplate()
    client.views_open(
		trigger_id = body['trigger_id'],
		view = current_form.create_form('init')
	)


#   -- Form Select Event --
@slack.action("type_list")
def select_form(ack, body, client):
    ack()

    selected = f"{body['actions'][0]['selected_option']['value']}"
    client.views_update(
		view_id = body["view"]["id"],
        hash = body["view"]["hash"],
		view = current_form.create_form(selected)
	)

#   -- Form Submit Event --
@slack.view("slack_form")
def submit_form(ack, view, client):
    ack()

    global current_form
    answers = {}
    input_blocks = view['state']['values']
    
    for block_id, value_id in input_blocks.items():
        if block_id == "type_menu":
            continue
        answers[block_id] = value_id['input']
    results = FormSubmission(current_form, answers)
    results.submit_form()
    current_form = None



if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)