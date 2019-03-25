import json, os

mainHome = os.environ['USERPROFILE']
listR = os.listdir(mainHome)
home = os.environ['USERPROFILE'] + '\\Downloads'
files = os.listdir(home)
sfile = ''
z = 0

with open('config.json') as config:
  setting = json.load(config)

for Chdir in listR:
    doubleCheck = os.path.isdir('%s\\%s' % (mainHome, Chdir))
    if doubleCheck == True: 
        print('this is big test man %s + %s' % (Chdir, z))
        z = z + 1
    elif doubleCheck == False:
      pass
# for setting in setting['folder']:

# #   if setting['sort'] == False:
