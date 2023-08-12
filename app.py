from dotenv import dotenv_values
from flask import Flask, request
from flaskext.mysql import MySQL
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from app.form_process import FormProcess
from app.form_submission import FormSubmission

config = dotenv_values(".form_env")

form = FormProcess()
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
    return "200 OK"

@app.route('/slack-api/events', methods = ['POST'])
def slack_events():
    response = slack_handler.handle(request)
    return response

#   -- Form view call route. --
@app.route('/slack-api/form', methods = ['POST'])
def slack_form():
    response = slack_handler.handle(request)
    return response

#   -- Form submit post route --
@app.route('/slack-api/form-submit', methods = ['POST'])
def slack_submission():
    response = slack_handler.handle(request)
    return response



#   ========================
#   || Event Section      ||
#   ========================

#   -- Form Select Event --
@slack.command("/form")
def selection_message(ack, client, say):
    ack()

    message = say(blocks = form.select_form_type())
    form.set_channel_start_time(channel = message.get('channel'), ts = message.get('ts'))

@slack.action("type_list")
def write_form(ack, body, client):
	ack()

	command = f"{body['actions'][0]['selected_option']['value']}"
	client.views_open(
		trigger_id = body['trigger_id'],
		view = form.create_form(command)
	)

#   -- Form Submit Event --
@slack.view("slack_form")
def submit_form(ack, view, client):
    ack()

    msg_channel, msg_ts = form.get_channel_start_time()
    client.chat_delete(channel = msg_channel, ts = msg_ts)

    answers = {}
    input_blocks = view['state']['values']
    for block_id, value_id in input_blocks.items():
        answers[block_id] = value_id['input']
    results = FormSubmission(form, answers)
    results.submit_form()



if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)