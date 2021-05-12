from flask import Flask, g, jsonify, render_template, request
from flask_cors import CORS
from werkzeug import exceptions
import sqlite3
from controllers import urls


app = Flask(__name__)
CORS(app)

DATABASE = 'database/database.db'

@app.route("/", methods=['GET','POST'])
def homepage():
  if request.method == 'GET': 
    init_db()
    return render_template('home.html')
  elif request.method == 'POST':
    response = urls.create(request)
    return render_template('home.html')

@app.route("/aliases")
def aliases(): 
    fns = {
            'GET': urls.all
    }
    resp, code = fns[request.method](request)
    return render_template('all_urls.html', content=resp), code


# DATABASE setup
def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = sqlite3.connect(DATABASE)
  return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
  with app.app_context():
    db = get_db()
    with app.open_resource('database/schema.sql', mode='r') as f:
      db.cursor().executescript(f.read())
    db.commit()

def query_db(query, args=(), one=False):
  cur = get_db().execute(query, args)
  get_db().commit()
  rv = cur.fetchall()
  cur.close()
  return (rv[0] if rv else None) if one else rv




# if __name__ == "__main__":
#     app.run(debug=True)

