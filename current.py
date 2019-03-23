import os, shutil, fnmatch, json

listR = os.listdir(os.environ['USERPROFILE'])
home = os.environ['USERPROFILE'] + '\\Downloads'
files = os.listdir(home)
sfile = ''

with open('config.json') as config:
  data = json.load(config)

# for sfile in files:
#     filename, fileExtension = os.path.splitext('%s\\%s' % (home, sfile))
#     check = os.path.isdir('%s\\%s' % (home, sfile))
#     exists = os.path.exists(home + '\\' + fileExtension)
#     fileExtensionRemoved = fileExtension.replace('.', '')

#     if check == True:
#       print('%s is a folder and will not be moved' %(sfile))
#     elif check == False:
#       print('file (%s) with the extension of (%s)' % (sfile, fileExtension))
      
#       if exists == True:
#         print('Folder %s already exists, not creating' %(fileExtension))
#         try:
#             shutil.move('%s\\%s' % (home, sfile), '%s\\%s\\%s' %(home, fileExtensionRemoved, sfile))
#         except:
#           print('And error has occured moving %s to %s\\%s' % (sfile, home, fileExtensionRemoved)) 
      
#       elif exists == False:
#         os.mkdir(home + '\\' + fileExtensionRemoved)
#         try:
#             shutil.move('%s\\%s' % (home, sfile), '%s\\%s\\%s' % (home, fileExtensionRemoved, sfile))
#         except:
#           print('And error has occured moving %s to %s\\%s' %(sfile, home, fileExtensionRemoved))