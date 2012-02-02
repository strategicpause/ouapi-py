from ouapi.auth import Authentication
from ouapi.site import Site

api_url = 'nickpeters.omniupdate.com'
api_key = '12345'
api_secret = '12345'
username = 'npeters'
params = {'api_url': api_url, 'api_key': api_key, 
          'api_secret': api_secret, 'username': username}
a = Authentication(params)
config = a.login()

print 'Printing a list of of existing sites.'
sites = Site.list(config)
for s in sites:
  site = Site(config, s)
  values = site.view()
  print values
  
print 'Creating a new site'
values['name'] = config['token']
values['account'] = 'Gallena'
site = Site(config, values)
print 'Save: ', site.save()
print 'Updating existing site'
site.set('username','testusername')
print 'Save: ', site.save()
print 'View: ', site.view()
print 'Delete: ', site.delete()
