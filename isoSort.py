
import os 
import shutil
import fnmatch


isoLocal = "%userprofile%\\Downloads\\iso"
exeLocal = "%userprofile%\\Downloads\\exe"
svgLocal = "%userprofile%\\Downloads"
wordLocal = "%userprofile%\\Downloads"
zippLocal = "%userprofile%\\Downloads"
rainmeterLocal = "%userprofile%\\Downloads"
powerpointLocal = "%userprofile%\\Downloads"
jpgLocal = "%userprofile%\\Downloads"
miscLocal = "%userprofile%\\Downloads"
location = r"%userprofile%\Downloads"



files = os.listdir(location)

print(os.curdir())


 for svile in files:

     iso = fnmatch.fnmatch(svile, '*.iso')
     exe = fnmatch.fnmatch(svile, '*.exe')
     svg = fnmatch.fnmatch(svile, '*.svg')
     word = fnmatch.fnmatch(svile, '*.docx')
     zipp = fnmatch.fnmatch(svile, '*.zip')
     rainmeter = fnmatch.fnmatch(svile, '*.rmskin')
     powerpoint = fnmatch.fnmatch(svile, '*.pptx')
     jpg = fnmatch.fnmatch(svile, '*.jpg')
     misc = fnmatch.fnmatch(svile, '*.*')

     if iso == True:
         shutil.move(location + '\\' + svile, isoLocal)
     elif exe == True:
         shutil.move(location + '\\' + svile, exeLocal)
     elif svg == True:
         shutil.move(location + '\\' + svile, svgLocal)
     elif word == True:
         shutil.move(location + '\\' + svile, wordLocal)
     elif zipp == True:
         shutil.move(location + '\\' + svile, zippLocal)
     elif rainmeter == True:
         shutil.move(location + '\\' + svile, rainmeterLocal)
     elif powerpoint == True:
         shutil.move(location + '\\' + svile, powerpointLocal)
     elif jpg == True:
         shutil.move(location + '\\' + svile, jpgLocal)
     else:
         shutil.move(location + '\\' + svile, miscLocal)
