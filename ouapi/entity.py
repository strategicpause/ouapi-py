import httplib, json, urllib

class OUEntity(object):
  def __init__(self, config = {}, columns = {}):
    self.api_url = config['api_url'] if 'api_url' in config else None
    self.api_token = config['token'] if 'token' in config else None
    self.columns = columns
    self.conn = None
    self.headers = {'Content-type': 'application/x-www-form-urlencoded', 
                    'Accept': 'text/plain'}
    self.values = {}
    
  def __setup(self):
    if self.conn == None:
      if self.api_url == None:
        raise Exception('No API Url has been given.')
      self.conn = httplib.HTTPConnection(self.api_url)
      #self.conn.set_debuglevel(1)

  def set_values(self, json={}):
    self.values = dict((key, value) for key, value in json.iteritems() 
      if key in self.columns)
    return self.values

  def set(self, name, value):
    if name in self.columns:
      self.values[name] = value

  def get(self, name):
    return self.values[name] if name in self.values else None

  def request(self, method='POST', body='', params={}):
    self.__setup()
    params = self.encode_params(params)
    body = body + ';jsessionid=' + self.api_token
    if method == 'GET':
      body = body + '?' + params
      self.conn.request(method, body,headers=self.headers)
    else:
      self.conn.request(method, body, params, self.headers)
    response = self.conn.getresponse()
    if response.status == 200:
      data = response.read()
      return json.loads(data)
    else:
      print response.status, response.reason
      print response.read()
      return None

  def encode_params(self, params):
    params = dict((k,v) for k,v in params.iteritems() if v != None)
    return urllib.urlencode(params)
