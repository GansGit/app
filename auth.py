import bottle
from bottle import route, run, template, redirect, request, get, auth_basic, abort, response, post
import base64


@route ('/')


def check(u,p):
    

  return True  
    

@auth_basic(check)

def home():
    return 'coll'
run (host='0.0.0.0', port=80, debug=True, reloader=True)
