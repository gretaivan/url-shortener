from werkzeug.exceptions import BadRequest
from flask import Flask, jsonify, redirect, request, url_for
import sqlite3
import app
from helpers import url_shortener

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

    exists = find_by_url(new_record)
    print(exists)
    if exists == []:
      alias = url_shortener.generator()
      return_value = app.query_db('insert into urls (actual_url, alias_url) values (?, ?);', (new_record, alias))
      check_value = app.query_db('select actual_url, alias_url from urls where alias_url = (?);', (alias,))
      return check_value, 201
    else:
      alias = exists[0][2]
      return alias, 202

def find_by_url(url):
  try:
    return app.query_db('select * from urls where actual_url = (?);', (url,))
  except:
    raise BadRequest(f"The URL {url} does not exist")


# def find_by_alias(alias):
#   try:
#     return app.query_db('select * from urls where alias_url = (?);', (alias,))
#   except:
#     raise BadRequest(f"The URL alias {alias} does not exist")

