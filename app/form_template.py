import copy
import json
from dotenv import dotenv_values
from flask import Flask, request
from flaskext.mysql import MySQL

config = dotenv_values(".form_env")

app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = config['MYSQL_LOCAL_HOST']
app.config['MYSQL_DATABASE_USER'] = config['MYSQL_LOCAL_USER']
app.config['MYSQL_DATABASE_DB'] = config['MYSQL_LOCAL_DB']
app.config['MYSQL_DATABASE_PASSWORD'] = config['MYSQL_LOCAL_PASSWORD']
mysql = MySQL(app)

class FormTemplate:
    def __init__(self):
        #   -- Open Database Connection. --
        conn = mysql.connect()
        cursor = conn.cursor()

        #   -- Execute SQL Commands --
        #   cursor = mysql.connection.cursor()
        query = f"SELECT type FROM form_templates WHERE NOT type = 'init';"
        cursor.execute(query)
        data_rows = cursor.fetchall()

        #   -- Close Database Connection. --
        cursor.close()
        conn.close()

        self.type_list = [command[0] for command in data_rows]
        self.type = None
        self.template = {
            #   Static Form Template
            "type": "modal",
            "callback_id": "slack_form",
            "title": {
                "type": "plain_text",
                "text": "Slack E-mail Form",
                "emoji": True
            },
            #   Dynamic Form Input Blocks
            "blocks": [
                {
                    "type": "section",
                    "block_id": "type_menu",
                    "text": {
                        "type": "mrkdwn",
                        "text": " "
                    },
                    "accessory": {
                        "type": "static_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Form List",
                            "emoji": True
                        },
                        "options": [
                            {
                                "text": {
                                    "type": "plain_text",
                                    "text": f"{f_type}",
                                    "emoji": True
                                },
                                "value": f"{f_type}"
                            }
                            for f_type in [
                                data_col[0] for data_col in data_rows
                            ]
                        ],
                        "action_id": "type_list"
                    }
                },
                {
                    "type": "divider",
                    "block_id": "divider"
                }
            ]
        }

    def create_form(self, command):
        view = copy.deepcopy(self.template)

        #   -- Open Database Connection. --
        conn = mysql.connect()
        cursor = conn.cursor()

        #   -- Execute SQL Commands --
        #   cursor = mysql.connection.cursor()
        query = f"SELECT type, template FROM form_templates WHERE type = '{command}';"
        cursor.execute(query)
        data_row = cursor.fetchone()

        #   -- Close Database Connection. --
        cursor.close()
        conn.close()

        self.type = data_row[0]

        if command != "init":
            view["submit"] = {
                "type": "plain_text",
                "text": "Submit Form",
                "emoji": True
            }
            view["close"] = {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            }
        for block in json.loads(data_row[1]):
            view['blocks'].append(block)
        return view