import json
from flask import Flask, request
from dotenv import dotenv_values
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
        query = f"SELECT type FROM form_templates;"
        cursor.execute(query)
        data_rows = cursor.fetchall()

        #   -- Close Database Connection. --
        cursor.close()
        conn.close()

        self.type_list = [command[0] for command in data_rows]
        self.type = None
        self.shape = {
            #   Static Form Template
            "type": "modal",
            "callback_id": "slack_form",
            "title": {
                "type": "plain_text",
                "text": "Slack E-mail Form",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit Form",
                "emoji": True
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
                "emoji": True
            },
            #   Dynamic Form Input Blocks
            "blocks": None
        }
    
    def create_form(self, command):
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
        self.shape["blocks"] = json.loads(data_row[1])
        return self.shape