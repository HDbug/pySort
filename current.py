import os, shutil, fnmatch

home = os.environ['USERPROFILE'] + '\\Downloads'
files = os.listdir(home)
sfile = ''

def checkR(uinput):
    fnmatch.fnmatch(sfile, uinput)

for sfile in files:
    filename, fileExtension = os.path.splitext('%s\\%s' % (home, sfile))
    check = os.path.isdir('%s\\%s' % (home, sfile))
    exists = os.path.exists(home + '\\' + fileExtension)
    fileExtensionRemoved = fileExtension.replace('.', '')
    #fnmatch.fnmatch(sfile, )

    if check == True:
      print('%s is a folder' %(sfile))
    elif check == False:
      print('file (%s) with the extension of (%s)' % (sfile, fileExtension))
      if exists == True:
        print('Folder %s already exists, not creating' %(fileExtension))
      elif exists == False:
        os.mkdir(home + '\\' + fileExtensionRemoved)
        