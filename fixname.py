#!/usr/bin/env python
# encoding: utf-8 
#
import os
import sys
import os.path
import re

def filtered(dirpath, filename): 
    return filename.endswith( ('.avi','.wmv','.mp4','.mkv','.rmvb') )

def rename(filename):
    fn = filename.replace('+',' ').replace('%5B','[').replace('%5D',']').replace('%28','(').replace('%29',')').replace('%40','@')
        #TODO: make a general %xx to char replace?
    return re.sub(r'[ ]+', ' ', fn) #not usable as ruby's gsub

#Use "batch_rename.py ." cannot get 1st argument '.'
#But if changed to "C:\Python27\python files_batch_rename.py .", can got the '.', doesn't know why
if len(sys.argv)<>2:
    print "Usgae C:\Python27\Python %s <base_dir>" % (sys.argv[0], sys.argv[1])
    sys.exit(0)

base_dir = sys.argv[1]
recursive = False

print "base_dir=[%s], recursive=[%s]" % (base_dir, str(recursive))

for dirpath, subdirnames, filenames in os.walk(base_dir, topdown=True):
    os.chdir( dirpath )
        #Fuck, why cannot use `cwd`(c will means change)?
    if not recursive:
            for filename in filenames:
                if filtered(dirpath, filename):
                    newfilename = rename(filename)
                    print "rename %s to %s" % (filename, newfilename)
                    os.rename(filename, newfilename)
    else:
        pass #TODO

