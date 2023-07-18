#   ========================
#   || Library Imports    ||
#   ========================

# import json
from dotenv import dotenv_values
from flask import Flask, request
from flaskext.mysql import MySQL
#   from flask_mysqldb import MySQL
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from form_template import FormTemplate
from form_submission import FormSubmission



#   ========================
#   || Config Loading     ||
#   ========================
config = dotenv_values(".form_env")



#   ========================
#   || App Initialization ||
#   ========================

form = FormTemplate()
app = Flask(__name__)
#   app.config['MYSQL_HOST'] = config['MYSQL_LOCAL_HOST']
#   app.config['MYSQL_USER'] = config['MYSQL_LOCAL_USER']
#   app.config['MYSQL_DB'] = config['MYSQL_LOCAL_DB']
#   app.config['MYSQL_PASSWORD'] = config['MYSQL_LOCAL_PASSWORD']
# app.config['MYSQL_DATABASE_HOST'] = config['MYSQL_LOCAL_HOST']
# app.config['MYSQL_DATABASE_USER'] = config['MYSQL_LOCAL_USER']
# app.config['MYSQL_DATABASE_DB'] = config['MYSQL_LOCAL_DB']
# app.config['MYSQL_DATABASE_PASSWORD'] = config['MYSQL_LOCAL_PASSWORD']
# mysql = MySQL(app)
slack = App(
    token = config["SLACK_BOT_TOKEN"],
    signing_secret = config["SLACK_SIGNING_SECRET"]
)
slack_handler = SlackRequestHandler(slack)
form = FormTemplate()



#   ========================
#   || Route Section      ||
#   ========================
@app.route('/', methods = ['GET'])
def slash_root():
    return "Ok"
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

#   -- Form Write Event --
@slack.command("/form")
def write_form(ack, body, client, say):
    ack()
    
    command = body.get('text')
    if command in form.type_list:
        client.views_open(
            trigger_id = body['trigger_id'],
            view = form.create_form(command)
        )
    else:
        say('Wrong Command!!!')

#   -- Form Submit Event --
@slack.view("slack_form")
def submit_form(ack, view):
    ack()

    #   -- Payload Print --
    #   if 1==1:
    #       print(view)
    #       return

    answers = {}
    input_blocks = view['state']['values']
    for block_id, value_id in input_blocks.items():
        answers[block_id] = value_id['input']['value']
    results = FormSubmission(form, answers)
    results.submit_form()



if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)