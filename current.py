import os, shutil, fnmatch

home = os.environ['USERPROFILE'] + '\\Downloads'
files = os.listdir(home)
sfile = ''

def check(uinput):
    fnmatch.fnmatch()

for sfile in files:
    filename, fileExtension = os.path.splitext('%s\\%s' % (home, sfile))
    check = os.path.isdir('%s\\%s' % (home, sfile))
    #fnmatch.fnmatch(sfile, )

    if check == True:
      print('%s is a folder' %(sfile))
    elif check == False:
      print('file (%s) with the extension of (%s)' % (sfile, fileExtension))