from flask import Flask
import psycopg2

app = Flask(__name__)

URL = "postgresql://my_postgresql_6c81_user:EBU4t7ahZIXXQPdDtwy2BgJBvYF9X6zG@dpg-d7a70ufpm1nc73bvaqsg-a/my_postgresql_6c81"

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app. route('/db_test')
def testing():
    conn = psycopg2.connect(URL)
    conn. close()
    return "Database Connection Successful"

@app. route ('/db_create')
def creating():
    conn = psycopg2.connect(URL)
    cur = conn. cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball(
            First VARCHAR(255),
            Last VARCHAR(255),
            City VARCHAR(255),
            Name VARCHAR(255),
            Number INT
            );
    ''')
    conn.commit ()
    conn. close ()
    return "Basketball Table Successfully Created"
