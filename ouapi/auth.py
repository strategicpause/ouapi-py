import httplib, urllib, json

class Authentication:
  def __init__(self, params = {}):
    self.api_url = params['api_url']
    self.api_key = params['api_key']
    self.api_secret = params['api_secret']
    self.username = params['username']
    
  def login(self):
    params = urllib.urlencode({'api_key': self.api_key, 
                               'api_secret': self.api_secret, 
                               'username': self.username})
    headers = {'Content-type': 'application/x-www-form-urlencoded', 'Accept': 'text/plain'}
    conn = httplib.HTTPConnection(self.api_url)
    conn.request('POST', '/apiv1/authentication/api_login', params, headers)
    response = conn.getresponse()
    if response.status == 200:
      data = json.loads(response.read())
      if 'error' in data:
        error_message = data['error']['message']
        raise Exception(error_message)
      else:
        return {'api_url': self.api_url, 'token': data['token'], 'type': data['type']}
    else:
      print response.status, response.reason
      return None
