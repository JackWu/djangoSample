import httplib
import simplejson
import json

HOST = 'ws.ttagit.com:53777'
#HOST = '192.168.0.21:8080'
#WS_USER_NAME='jackwu2012'
#WS_PASSWORD='jackjack'
#WS_USER_NAME='dstinard'
#WS_PASSWORD='passpass'
#WS_USER_NAME='jeff'
#WS_PASSWORD='redwine'
LOCAL_USER_NAME = 'thefirstusername'
LOCAL_PASSWORD='ssss1111'


JSON_HEADERS = {'Content-type':'application/json; charset=utf-8'}

def create_an_ad(access_token, banner_url, ads_url, ads_location, user_reference):
	data = {'access_token':access_token, 'banner_image_url':banner_url, 'ads_url':ads_url, 'ads_location': ads_location, 'user_reference': user_reference}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/create-pro-market-ads', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def login():
#  data={'user_name':WS_USER_NAME, 'password':WS_PASSWORD}
#	data={'user_name':LOCAL_USER_NAME, 'password':LOCAL_PASSWORD}
	data = {'user_name':'jackwu2012', 'password':'jackjackjack'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/login', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	token = simplejson.loads(data)
	print json.dumps(token, sort_keys=True, indent=2)
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
	result = simplejson.loads(data)
	print json.dumps(result, sort_keys=True, indent=2)


def pro_acct_verifier(access_token):
	data = {'access_token': access_token}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/validate/pro-access', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	result = simplejson.loads(data)
	print json.dumps(result, sort_keys=True, indent=2)

def pro_market_acct_verifier(access_token):
	data = {'access_token':access_token}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/validate/pro-market-access', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def update_account(acct_type, user_id):
	if acct_type == 'pro':
		update_to_pro(user_id)
	elif acct_type == 'pro_market':
		update_to_pro_market(user_id)
	elif acct_type == 'normal':
		update_to_normal(user_id)
	else:
		print 'acct_type is not recognized'
		
def update_to_pro(user_id):
#	data = {'_id':user_id, 'secret_key':'UxNDBmZmU3YjZiNWYwNjRjOGI2ODU3ZmU0NDNiYmVlMzU1NjAxMWJkNjk4ODE5NDE', 'access_token':token}
	data = {'_id':user_id, 'secret_key':'UxNDBmZmU3YjZiNWYwNjRjOGI2ODU3ZmU0NDNiYmVlMzU1NjAxMWJkNjk4ODE5NDE'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/e5802cc2316edc823', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def update_to_pro_market(user_id, payment_msg):
	#data = {'_id':user_id, 'access_token':token, 'secret_key':'zZmZmRhZWY5OTdmYTgyMzg0YWFhNTM3NWUzZTMwZjMzOTMwYmIwODNhYjU0ZDNkOTk4NzhlMj'}
	data = {'_id':user_id, 'secret_key':'zZmZmRhZWY5OTdmYTgyMzg0YWFhNTM3NWUzZTMwZjMzOTMwYmIwODNhYjU0ZDNkOTk4NzhlMj', 'payment_msg':payment_msg}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/c730e4188d9b80a', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def update_to_normal(user_id):
#	data = {'_id':user_id, 'access_token':token, 'secret_key':'MjUxMzkxYmI5MWE2YzAxZGFjNjNjMTFmOTcyM2Q5MDI1ZmNjNDQ5Zj'}
	data = {'_id':user_id, 'secret_key':'MjUxMzkxYmI5MWE2YzAxZGFjNjNjMTFmOTcyM2Q5MDI1ZmNjNDQ5Zj'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/72b87d69468a2ea', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def cancel_pro(user_id):
	#data = {'_id':user_id, 'access_token':token, 'secret_key':'UxNDBmZmU3YjZiNWYwNjRjOGI2ODU3ZmU0NDNiYmVlMzU1NjAxMWJkNjk4ODE5NDE'}
	data = {'_id':user_id, 'secret_key':'UxNDBmZmU3YjZiNWYwNjRjOGI2ODU3ZmU0NDNiYmVlMzU1NjAxMWJkNjk4ODE5NDE'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/892401383b90a91f227eb58036af5b', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def cancel_pro_market(user_id):
	#data = {'_id':user_id, 'access_token':token, 'secret_key':'zZmZmRhZWY5OTdmYTgyMzg0YWFhNTM3NWUzZTMwZjMzOTMwYmIwODNhYjU0ZDNkOTk4NzhlMj'}
	data = {'_id':user_id, 'secret_key':'zZmZmRhZWY5OTdmYTgyMzg0YWFhNTM3NWUzZTMwZjMzOTMwYmIwODNhYjU0ZDNkOTk4NzhlMj'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/updateaccount/ebbfff8a00494dc719a9aa95', json_data, JSON_HEADERS)
	data = conn.getresponse().read()
	print data

def user_id_for_ads_full(access_token, user_id):
	data = {'user_id':user_id, 'access_token':access_token, 'active_opt':'all'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/user-id-for-ads-full', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def user_id_for_ads_ids(access_token, user_id):
	data = {'user_id':user_id, 'access_token':access_token, 'active_opt':'all'}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/user-id-for-ads-ids', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def get_a_single_ad_full_info(access_token, ads_id):
	data = {'ads_id':ads_id, 'access_token':access_token}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/get-single-ad-full-info', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	token = simplejson.loads(response)
	print json.dumps(token,sort_keys=True, indent=2)

def activate_an_ad(access_token, ads_id):
	data = {'access_token':access_token, 'ads_id':ads_id}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/activate-ads', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def deactivate_an_ad(access_token, ads_id):
	data = {'access_token':access_token, 'ads_id':ads_id}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/deactivate-ads', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def del_pro_market_ads(access_token, ads_id):
	data = {'access_token':access_token, 'ads_id':ads_id}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/delete-pro-market-ads', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def get_a_mobile_ad():
	data = {}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/get-a-mobile-ad', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def get_a_slide_ad():
	data = {}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/get-a-slide-ad', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def get_an_ext_ad():
	data = {}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/get-an-ext-ad', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def get_a_homepage_ad():
	data = {}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/get-a-homepage-ad', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def get_a_profile_ad():
	data = {}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/get-a-profile-ad', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def del_a_pro_market_ad(access_token, ads_id):
	data = {'access_token':access_token, 'ads_id':ads_id}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/delete-pro-market-ads', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def update_ads_status(access_token, ads_id, new_status):
	data = {'access_token':access_token, 'ads_id':ads_id, 'new_status':new_status}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/update-ads-status', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def update_ads_image_url(access_token, ads_id, banner_url):
	data = {'access_token':access_token, 'ads_id':ads_id, 'banner_image_url':banner_url}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/update-ads-image-url', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)

def update_ads_url(access_token, ads_id, ads_url):
	data = {'access_token':access_token, 'ads_id':ads_id, 'ads_url':ads_url}
	json_data = simplejson.dumps(data)
	conn = httplib.HTTPConnection(HOST)
	conn.request('POST', '/ads/update-ads-url', json_data, JSON_HEADERS)
	response = conn.getresponse().read()
	result = simplejson.loads(response)
	print json.dumps(result, sort_keys=True, indent=2)
