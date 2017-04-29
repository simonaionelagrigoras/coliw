import webbrowser,facebook
from requests_oauthlib import OAuth2Session
from requests_oauthlib.compliance_fixes import facebook_compliance_fix

# Credentials you get from registering a new application
client_id = '1387733244617941'
client_secret = '0aebb282152cbca66116bd5707d8b0c5'

# OAuth endpoints given in the Facebook API documentation
authorization_base_url = 'https://www.facebook.com/dialog/oauth'
token_url = 'https://graph.facebook.com/oauth/access_token'
redirect_uri = 'http://www.myserver.com/coliw'     # Should match Site URL


facebook = OAuth2Session(client_id, redirect_uri=redirect_uri)
facebook = facebook_compliance_fix(facebook)

# Redirect user to Facebook for authorization
authorization_url, state = facebook.authorization_url(authorization_base_url)
webbrowser.open_new_tab(authorization_url)

print(state)
# Get the authorization verifier code from the callback url
redirect_response = 'https://www.myserver.com/coliw'
#
# # Fetch the access token
#facebook.fetch_token(token_url, client_secret=client_secret,
#                   authorization_response=redirect_response)

# Fetch a protected resource, i.e. user profile
r = facebook.get('https://graph.facebook.com/me?')
print(r.content)