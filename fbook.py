import facebook
import urllib
from urllib import request
import json


# Parameters of your app and the id of the profile you want to mess with.
# FACEBOOK_APP_ID     = '1387733244617941'
# FACEBOOK_APP_SECRET = '0aebb282152cbca66116bd5707d8b0c5'
FACEBOOK_APP_ID = '506276502849459'
FACEBOOK_APP_SECRET = '0eab8f2933a00ef259eaa712d5716b5b'


# Trying to get an access token. Very awkward.
oauth_args = dict(client_id     = FACEBOOK_APP_ID,
                  client_secret = FACEBOOK_APP_SECRET,
                  grant_type    = 'client_credentials')
request_params = urllib.parse.urlencode(oauth_args)
 # data should be bytes
req = urllib.request.Request('https://graph.facebook.com/oauth/access_token?', request_params.encode('ascii'))
data = urllib.request.urlopen(req).read().decode("utf-8")
data = json.loads(data)
print(data)
print(data.get('access_token'))
#acc_token = facebook(FACEBOOK_APP_ID, FACEBOOK_APP_SECRET)
#print(acc_token)

graph = facebook.GraphAPI(access_token="EAAHMdK8cR7MBAI42ZAhPY04ZBo4amUyKKZCMPSkblF56wqO1xngmaTSZChb1xRa5Psuk4QbnjR7duD4qEczHeoPTFFs6gfQXnaN1JwjstUWHFWWNDnPMfuhysx5C4ZCIMmAkLpYI0FQIfbdQAYnNagZBOAil3GCnllKpjMLRqASV4qn5uDaQRFrV2O9XFZCPecZD", version='2.7')

# Get all of the authenticated user's friends
friends = graph.get_connections(id='me', connection_name='')
print(friends)