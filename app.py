from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = mysql.connector.connect(
            host='mysql-container',  # Will match the MySQL container name
            user='root',
            password='example',
            database='testdb'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        return f"Connected to MySQL! Current time: {result[0]}"
    except mysql.connector.Error as err:
        return f"Error: {err}"
