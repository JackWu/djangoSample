import httplib
import simplejson

HOST = 'ws.ttagit.com:53777'


JSON_HEADERS = {'Content-type':'application/json; charset=utf-8'}

def create_an_ad(access_token, banner_url, ads_url, ads_location):
	data = {'access_token':access_token, 'banner_image_url':banner_url, 'ads_url':ads_url, 'ads_location': ads_location}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/create-pro-market-ads', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def del_an_ad(ads_id)
	

def login():
	data = {'user_name':'rur', 'password':'ttagit!'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/login', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	token = simplejson.loads(data)
	print token
	return token['data']['user_data']['access_token']

def get_user_id(access_token):
	data = {'access_token':access_token}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/user/tokenforid', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	user_id = simplejson.loads(data)
	print user_id 
	return user_id['user_id']

def get_an_ad():
	data = {}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/get-a-random-ad', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data



