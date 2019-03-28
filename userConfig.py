import json, os

class system:
  mainHome = os.environ['USERPROFILE']
  listR = os.listdir(mainHome)
  home = os.environ['USERPROFILE'] + '\\Downloads'
  files = os.listdir(home)
  sfile = ''
  z = 0
  folders = []
  addedFolders = []

def main():
  addRequest()
  jsonAdd()

def addRequest():
  for i in range(len(system.folders)):
    userRequest = input('Would you like to add %s to the list of folders to edit? y/n: ' %(i))
    if userRequest == y or Y:
      system.addedFolders.append("%s\\%s" %(system.mainHome, i))
    elif userRequest == n or N:
      print('Not adding %s to the list' %(i))

def jsonAdd():
  for i in range(len(system.addedFolders)):
    with open('config.json') as config:
      loader = json.load(config)
    jsonIncrease["location"] = i
    with open('config.json', 'w+') as config:
      json.dump(jsonIncrease, config)

for Chdir in system.listR:
    doubleCheck = os.path.isdir('%s\\%s' % (system.mainHome, Chdir))

    if doubleCheck == True: 
      print('Adding %s to the folders list' %(Chdir))
      system.folders.append('%s\\%s' %(system.mainHome, Chdir))

    elif doubleCheck == False:
      pass

main()