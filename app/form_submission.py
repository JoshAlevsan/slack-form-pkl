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

class FormSubmission:
    def __init__(self, form, answers):
        self.form = form
        self.answers = answers
    
    def submit_form(self):
        #   Format Results To JSON
        answers_json = json.dumps(self.answers)
        answers_sql_json = json.dumps(answers_json)

        #   -- Open Database Connection. --
        conn = mysql.connect()
        cursor = conn.cursor()

        #   -- Execute SQL Commands --
        #   cursor = mysql.connection.cursor()
        query = f"INSERT INTO form_submission (type, answers) VALUES ('{self.form.type}', {answers_sql_json});"
        cursor.execute(query)
        conn.commit()

        #   -- Close Database Connection. --
        cursor.close()
        conn.close()