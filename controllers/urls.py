from werkzeug.exceptions import BadRequest
from flask import request, jsonify
import sqlite3
import app

def all(req):
  urls = app.query_db('select * from urls;')
  return urls, 200

# def show(req, uid):
#   fetch_result = find_by_alias(uid)
#   if fetch_result == []:
#     raise BadRequest(f"URL with alias of {uid} does not exist")
#   else:
#     return fetch_result, 200

def create(req):
    new_record = req.form['url']
    print(new_record)
    # found if actual url already exits
    # def exists():


    # if exists:
    #     alias = ""   # alias =  generate the alias url
    #     return_value = app.query_db('insert into urls (actual_url, alias_url) values (?, ?);', (new_record["url"], alias))
    #     check_value = app.query_db('select id from people where name = (?);', (new_person["name"],))
    #     return check_value, 201

# def find_by_alias(alias):
#   try:
#     return app.query_db('select * from urls where alias_url = (?);', (alias,))
#   except:
#     raise BadRequest(f"The URL alias {alias} does not exist")

