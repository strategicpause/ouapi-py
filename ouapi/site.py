from .entity import OUEntity

class Site(OUEntity):
  columns = ['name', 'address', 'username', 'password', 'ftp_root', 
            'ftp_home', 'ftp_path', 'image_path', 'trash_path',
            'template_root', 'local_template_troot', 'use_local',
            'http_root']

  def __init__(self, config={}, values={}):
    super(Site, self).__init__(config, Site.columns)
    self.set_values(values)
    self.account = values['account'] if 'account' in values else None
    
  def view(self):
    name = self.get('name')
    if name == None:
      return
    params = {'site': name}
    if self.account != None:
      params['user'] = self.account
    json = self.request('GET', '/apiv1/sites/view', params)
    return self.set_values(json)
    
  def delete(self):
    name = self.get('name')
    if name == None:
      return
    params = {'site': name}
    if self.account != None:
      params['user'] = self.account
    json = self.request('POST', '/apiv1/sites/delete', params)
    self.values = None
    return json
  
  def save(self):
    name = self.get('name')
    if name == None:
      return
    if self.account == None:
      params = self.values
    else:
      params = dict(self.values.items() + {'user': self.account}.items())
    json = self.request('POST', '/apiv1/sites/save', params)
    return json
  
  @staticmethod
  def list(config={}, account=None):
    entity = OUEntity(config)
    params = {} if account == None else { 'user': account }
    json = entity.request('GET', '/apiv1/sites/list', params)
    return json
    
      
  
      
    
