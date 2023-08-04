import json
import threading
import mysql.connector
from dotenv import dotenv_values
# from flask import Flask, request
# from flaskext.mysql import MySQL

config = dotenv_values(".settings_env")

# app = Flask(__name__)
conn = mysql.connector.connect(
    host = config['MYSQL_LOCAL_HOST'],
    user = config['MYSQL_LOCAL_USER'],
    database = config['MYSQL_LOCAL_DB'],
    passwd = config['MYSQL_LOCAL_PASSWORD']
)
# app.config['MYSQL_DATABASE_HOST'] = config['MYSQL_LOCAL_HOST']
# app.config['MYSQL_DATABASE_USER'] = config['MYSQL_LOCAL_USER']
# app.config['MYSQL_DATABASE_DB'] = config['MYSQL_LOCAL_DB']
# app.config['MYSQL_DATABASE_PASSWORD'] = config['MYSQL_LOCAL_PASSWORD']
# mysql = MySQL(app)

with open('template.json') as test_file:
    file_contents = test_file.read()

def select_one():
    cursor = conn.cursor()

    query = f"SELECT * FROM form_templates;"
    cursor.execute(query)
    data = json.loads(cursor.fetchone()[0])
    print(data)


    cursor.close()
    conn.close()

def delete_all():
    cursor = conn.cursor()

    query = f"DELETE FROM form_submissions;"
    cursor.execute(query)
    query = f'ALTER TABLE form_submissions AUTO_INCREMENT = 1;'
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def insert_json():
    cursor = conn.cursor()

    data = json.loads(file_contents)
    json_data = json.dumps(data)
    sql_json_data = json.dumps(json_data)

    query = f'INSERT INTO form_templates (type, template) VALUES ("init", {sql_json_data});'
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def run_app():
    app.run(port = 3000, debug = True)

status  = 1
print(f"DB Settings Started({status}).\n\n")
while status == 1:
    print("""
> SELECT ONE OF THE COMMAND BELOW TO RUN:

-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|| 1 ---> INSERT NEW TEMPLATE           ||
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|| 2 ---> TRUNCATE SUBMISSIONS          ||
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|| 0 ---> EXIT SETTINGS                 ||
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
(HINT: TYPE THE NUMBER AND HIT ENTER.)
""")
    command = int(input("> "))
    match command:
        case 1:
            pass
        case 2:
            pass
        case 0:
            status = 0
        case other:
            print("\n> RESPONSE: COMMAND UNAVAILABLE!")
print(f"DB Settings Closed({status}).\n\n")

# if __name__ == "__main__":
#     flask_thread = threading.Thread(target=run_app)
#     flask_thread.start()

#     request.environ.get('werkzeug.server.shutdown')
#     flask_thread.join()