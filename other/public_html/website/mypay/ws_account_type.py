import httplib
import simplejson

HOST = 'ws.ttagit.com:53777'

JSON_HEADERS = {'content-type':'application/json; charset=utf-8'}

def update_to_pro(user_id):
	data={'secret_key':'aaa', '_id':'aaa'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', /updateaccount/', json_data, JSON_HEADERS)
	value_data = json.loads(conn.getresponse().read())
	return value_data['result']

def update_to_pro_market(user_id):
  data={'secret_key':'aaa', '_id':'aaa'}
  json_data = simplejson.dumps(data)
  conn = httplib.HTTPConnection(HOST)
  conn.request('POST', /updateaccount/', json_data, JSON_HEADERS)
  value_data = json.loads(conn.getresponse().read())
  return value_data['result']


def update_to_normal(user_id):
  data={'secret_key':'aaa', '_id':'aaa'}
  json_data = simplejson.dumps(data)
  conn = httplib.HTTPConnection(HOST)
  conn.request('POST', /updateaccount/', json_data, JSON_HEADERS)
  value_data = json.loads(conn.getresponse().read())
  return value_data['result']
