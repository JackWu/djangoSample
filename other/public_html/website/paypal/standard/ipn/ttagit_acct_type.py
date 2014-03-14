import httplib
import simplejson
import logging

HOST = 'ws.ttagit.com:53777'
JSON_HEADERS = {'Content-type':'application/json; charset=utf-8'}

logger = logging.getLogger("dev.ttagit.logger")

def pro_acct_verifier(access_token):
	logger.info('ipn->ttagit_acct_type->pro_acct_verifier')
	data = {'access_token': access_token}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/validate/pro-access', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	logger.info(data)

def pro_market_acct_verifier(access_token):
	logger.info('ipn->ttagit_acct_type->pro_market_acct_verifier')
	data = {'access_token':access_token}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/validate/pro-market-access', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	logger.info(data)

def update_account(acct_type, user_id):
	logger.info('ipn->ttagit_acct_type->update_account')
	if acct_type == 'ttagit_pro':
		update_to_pro(user_id)
	elif acct_type == 'ttagit_pro_market':
		update_to_pro_market(user_id)
	elif acct_type == 'normal':
		update_to_normal(user_id)
	else:
		logger.info('acct_type is not recognized')

def cancel_account(acct_type, user_id):
	logger.info('ipn->ttagit_acct_type->cancel_account')
	if acct_type == 'ttagit_pro':
		cancel_pro(user_id)
	elif acct_type == 'ttagit_pro_market':
		cancel_pro_market(user_id)
	else:
		logger.info('acct_type is not recognized')

def update_to_pro(user_id):
	logger.info('ipn->ttagit_acct_type->update_to_pro')
	data = {'_id':user_id, 'secret_key':'UxNDBmZmU3YjZiNWYwNjRjOGI2ODU3ZmU0NDNiYmVlMzU1NjAxMWJkNjk4ODE5NDE'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/e5802cc2316edc823', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	logger.info(data)

def update_to_pro_market(user_id):
	logger.info('ipn->ttagit_acct_type->update_to_pro_market')
	data = {'_id':user_id, 'secret_key':'zZmZmRhZWY5OTdmYTgyMzg0YWFhNTM3NWUzZTMwZjMzOTMwYmIwODNhYjU0ZDNkOTk4NzhlMj'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/c730e4188d9b80a', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	logger.info(data)

def update_to_normal(user_id):
	logger.info('ipn->ttagit_acct_type->update_to_normal')
	data = {'_id':user_id, 'secret_key':'MjUxMzkxYmI5MWE2YzAxZGFjNjNjMTFmOTcyM2Q5MDI1ZmNjNDQ5Zj'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/72b87d69468a2ea', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	logger.info(data)

def cancel_pro(user_id):
	logger.info('ipn->ttagit_acct_type->cancel_pro')
	data = {'_id':user_id, 'secret_key':'UxNDBmZmU3YjZiNWYwNjRjOGI2ODU3ZmU0NDNiYmVlMzU1NjAxMWJkNjk4ODE5NDE'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/892401383b90a91f227eb58036af5b', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	logger.info(data)

def cancel_pro_market(user_id):
	logger.info('ipn->ttagit_acct_type->cancel_pro_market')
	data = {'_id':user_id, 'secret_key':'zZmZmRhZWY5OTdmYTgyMzg0YWFhNTM3NWUzZTMwZjMzOTMwYmIwODNhYjU0ZDNkOTk4NzhlMj'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/ebbfff8a00494dc719a9aa95', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	logger.info(data)
