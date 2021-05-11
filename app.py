from flask import Flask
from flask_cors import CORS
from werkzeug import exceptions
import sqlite3

app = Flask(__name__)
CORS(app)



@app.route("/")
def homepage(): 
    return "Welcome!"

if __name__ == "__main__":
    app.run(debug=True)

