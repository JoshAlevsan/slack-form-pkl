import json
from dotenv import dotenv_values
from flask import Flask
from flaskext.mysql import MySQL

config = dotenv_values(".settings_env")

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = config['MYSQL_LOCAL_HOST']
app.config['MYSQL_DATABASE_USER'] = config['MYSQL_LOCAL_USER']
app.config['MYSQL_DATABASE_DB'] = config['MYSQL_LOCAL_DB']
app.config['MYSQL_DATABASE_PASSWORD'] = config['MYSQL_LOCAL_PASSWORD']
mysql = MySQL(app)

with open('template.json') as test_file:
    file_contents = test_file.read()

def select_one():
    conn = mysql.connect()
    cursor = conn.cursor()

    query = f"SELECT * FROM form_templates;"
    cursor.execute(query)
    data = json.loads(cursor.fetchone()[0])
    print(data)


    cursor.close()
    conn.close()

def delete_all():
    conn = mysql.connect()
    cursor = conn.cursor()

    query = f"DELETE FROM form_templates;"
    cursor.execute(query)
    query = f'ALTER TABLE form_templates AUTO_INCREMENT = 1;'
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

def insert_json():
    conn = mysql.connect()
    cursor = conn.cursor()

    data = json.loads(file_contents)
    json_data = json.dumps(data)
    sql_json_data = json.dumps(json_data)

    query = f'INSERT INTO form_templates (type, template) VALUES ("blank form", {sql_json_data});'
    cursor.execute(query)
    conn.commit()

    cursor.close()
    conn.close()

# select_one()
# delete_all()
insert_json()

if __name__ == "__main__":
    app.run(port = 3000, debug = True)