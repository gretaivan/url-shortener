from flask import Flask, g, jsonify, render_template, redirect, request, url_for
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
    return render_template('home.html')
  elif request.method == 'POST':
    response, code = urls.create(request)
    if code == 201:
      return render_template('home.html')
    else: 
      return redirect(url_for('aliases', alias=response))

@app.route("/aliases")
@app.route("/aliases/<alias>", methods=['GET'])
def aliases(alias=None): 
    fns = {
            'GET': urls.all
    }
    if alias == None: 
      resp, code = fns[request.method](request)
      return render_template('all_urls.html', content=resp), code
    else:
      return render_template('alias.html', alias=alias)
  
  

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

def create_app():
    app = Flask(__name__)
    with app.app_context():
        init_db()
    return app

create_app()



# if __name__ == "__main__":
#     app.run(debug=True)

