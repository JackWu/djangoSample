import httplib
import simplejson

HOST = 'ws.ttagit.com:53777'
JSON_HEADERS = {'Content-type':'application/json; charset=utf-8'}

def pro_acct_verifier(access_token):
	data = {'access_token': access_token}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/validate/pro-access', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def pro_market_acct_verifier(access_token):
	data = {'access_token':access_token}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/validate/pro-market-access', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def update_to_pro(user_id):
	data = {'_id':user_id, 'secret_key':'UxNDBmZmU3YjZiNWYwNjRjOGI2ODU3ZmU0NDNiYmVlMzU1NjAxMWJkNjk4ODE5NDE'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/e5802cc2316edc823', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def update_to_pro_market(user_id):
	data = {'_id':user_id, 'secret_key':'zZmZmRhZWY5OTdmYTgyMzg0YWFhNTM3NWUzZTMwZjMzOTMwYmIwODNhYjU0ZDNkOTk4NzhlMj'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/c730e4188d9b80a', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def update_to_normal(user_id):
	data = {'_id':user_id, 'secret_key':'MjUxMzkxYmI5MWE2YzAxZGFjNjNjMTFmOTcyM2Q5MDI1ZmNjNDQ5Zj'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/72b87d69468a2ea', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def cancel_pro(user_id):
	data = {'_id':user_id, 'secret_key':'UxNDBmZmU3YjZiNWYwNjRjOGI2ODU3ZmU0NDNiYmVlMzU1NjAxMWJkNjk4ODE5NDE'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/892401383b90a91f227eb58036af5b', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def cancel_pro_market(user_id):
	data = {'_id':user_id, 'secret_key':'zZmZmRhZWY5OTdmYTgyMzg0YWFhNTM3NWUzZTMwZjMzOTMwYmIwODNhYjU0ZDNkOTk4NzhlMj'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/ebbfff8a00494dc719a9aa95', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

