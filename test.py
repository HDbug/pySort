import json, os

listR = os.listdir(os.environ['USERPROFILE'])
home = os.environ['USERPROFILE'] + '\\Downloads'
files = os.listdir(home)
sfile = ''

with open('config.json') as config:
  data = json.load(config)

for Chdir in listR:
    doubleCheck = os.path.isdir('%s\\%s' % (listR, Chdir))
    if doubleCheck == False: 
        print('nah')
    else:
        print('this is big test man %s' % (doubleCheck))

# for setting in data['folder']:

# #   if setting['sort'] == False:
