from flask import Flask
import sqlite3
app = Flask(__name__)


@app.route("/")
def home():
    connection = sqlite3.connect('mondial.db') # establish database connection
    cursor = connection.cursor() # create a database query cursor

    city = "Stockholm"
    try:
        query ='SELECT * FROM Citypops WHERE city == (?);'
        cursor.execute(query, (city,))
        result = cursor.fetchall()
    except sqlite3.Error as e:
        print( "Error message:", e.args[0])
        connection.rollback()
        exit()
    
    return result
