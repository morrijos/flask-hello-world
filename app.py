from flask import Flask
import psycopg2

app = Flask(__name__)

# Render PostgreSQL Internal Database URL
url = "postgresql://my_postgresql_6c81_user:EBU4t7ahZIXXQPdDtwy2BgJBvYF9X6zG@dpg-d7a70ufpm1nc73bvaqsg-a/my_postgresql_6c81"


# Hello World
@app.route('/')
def home():
    return "Hello, World!"


# Database connection
@app.route('/db_test')
def db_test():
    conn = psycopg2.connect(url)
    conn.close()
    return "DB: Connection successful"


# Create basketball table
@app.route('/db_create')
def db_create():
    conn = psycopg2.connect(url)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS basketball(
            first VARCHAR(255),
            last VARCHAR(255),
            city VARCHAR(255),
            name VARCHAR(255),
            number INT
        );
    ''')
    conn.commit()
    conn.close()
    return "DB: Created basketball table"


# Insert data into basketball table
@app.route('/db_insert')
def db_insert():
    conn = psycopg2.connect(url)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO basketball (first, last, city, name, number)
        VALUES
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
    ''')
    conn.commit()
    conn.close()
    return "DB: Inserted values into basketball table"


# Select from basketball table
@app.route('/db_select')
def db_select():
    conn = psycopg2.connect(url)
    cur = conn.cursor()
    cur.execute('''
        SELECT * 
        FROM basketball;''')
    records = cur.fetchall()
    conn.close()
    response_string="" response_string+="<table>"
        for player in records: response_string+="<tr>"
            for info in player:
                response_string+="<td>{}</td>".format(info) 
            response_string+="</tr>" 
    response_string+="</table>"
    return response_string


# Drop basketball table
@app.route('/db_drop')
def db_drop():
    conn = psycopg2.connect(url)
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE basketball;
    ''')
    conn.commit()
    conn.close()
    return "DB: Dropped basketball table"


# Run locally
if __name__ == '__main__':
    app.run(debug=True)
