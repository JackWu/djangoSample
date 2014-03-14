import httplib
import json
import simplejson

JSON_HEADERS = {'Content-type':'application/json; charset=utf-8'}
HOST = 'localhost:8080'

def hello():  
  #variable pass to webservice
  data = {"id":"1"}
  json_data = simplejson.dumps(data)
  conn = httplib.HTTPConnection(HOST)
  conn.request('POST', '/test', json_data, JSON_HEADERS)
  data = conn.getresponse().read()
  token = simplejson.loads(data)
  print json.dumps(token, sort_keys=True, indent=2)
