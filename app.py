from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app. route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://my_postgresql_6c81_user:EBU4t7ahZIXXQPdDtwy2BgJBvYF9X6zG@dpg-d7a70ufpm1nc73bvaqsg-a/my_postgresql_6c81")
    conn. close()
    return "Database Connection Successful"
