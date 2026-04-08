from flask import Flask
import psycopg2

app = Flask(__name__)

URL = "postgresql://my_postgresql_6c81_user:EBU4t7ahZIXXQPdDtwy2BgJBvYF9X6zG@dpg-d7a70ufpm1nc73bvaqsg-a/my_postgresql_6c81"

@app.route('/')
def hello_world():
    return 'Hello, World!'


# Connect to Postgres instance
@app. route('/db_test')
def testing():
    conn = psycopg2.connect(URL)
    conn. close()
    return "Print: Database connection successful"



# Create DB
@app. route ('/db_create')
def creating():
    conn = psycopg2.connect(URL)
    cur = conn. cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS basketball (
            First VARCHAR(255),
            Last VARCHAR(255),
            City VARCHAR(255),
            Name VARCHAR(255),
            Number INT
            );
    ''')
    conn.commit ()
    conn. close ()
    return "Print: Basketball table successfully created"


# Add data to DB
@app. route ('/db_insert')
def creating():
    conn = psycopg2.connect(URL)
    cur = conn. cursor()
    cur.execute('''
        INSERT INTO basketball (First, Last, City, Name, Number)
            VALUES
            ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
            ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
            ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
            ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit ()
    conn. close ()
    return "Print: Basketball table successfully updated"


# Select data from DB
@app.route('/db_select')
def selecting():
    conn = psycopg2.connect(URL)
    cur = conn. cursor()
    cur.execute('''
        SELECT *
        FROM basketball;
    ''')
    records = cur.fetchall()
    conn.close() 
    response_string="" 
    response_string+="<table>"
    for player in records: 
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td>".format(info) 
        response_string+="</tr>" 
    response_string+="</table>"
    return response_string
