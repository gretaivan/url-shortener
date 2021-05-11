from flask import Flask
from flask_cors import CORS
from werkzeug import exceptions
import sqlite3

app = Flask(__name__)
CORS(app)

DATABASE = 'database/database.db'

@app.route("/")
def homepage(): 
    init_db()
    return "Welcome!"


def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
  return db

def init_db():
  with app.app_context():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()


if __name__ == "__main__":
    app.run(debug=True)

