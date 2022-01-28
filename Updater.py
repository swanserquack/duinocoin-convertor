#!/usr/bin/env python3
#######################################################
# Duino-Coin Convertor                                #
# https://github.com/swanserquack/duinocoin-convertor #
# No copyright                                        #
#######################################################

import requests
import os
import time
import shutil
import filecmp
from os import path, mkdir
from pathlib import Path

#Sets all the values we need
Updater = 'Update Resources'
Folder = 'Resources'
json1 = 'Resources/values.json'
json2 = 'Update Resources/values.json'
python1 = 'Convertor.py'
python2 = 'Update Resources/Convertor.py'
req1 = 'requirements.txt'
req2 = 'Update Resources/requirements.txt'
Complete = 'Update Complete'
values = "/values.json"

if not path.exists(Updater):
    mkdir(Updater)

if not path.exists(Folder):
    mkdir(Folder)

if not Path(Folder + values).is_file():   #If the values.json file does not exist then it creates it
    tempd = requests.get("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/Resources/values.json")
    with open(Folder + values, "wb") as f:
        f.write(tempd.content)  #Writes the values.json file

#Grabs the update files fromt the repository

if not Path(Updater + values).is_file():
    tempd = requests.get("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/Resources/values.json")
    with open(Updater + values, "wb") as f:
        f.write(tempd.content)

if not Path(Updater + "/Convertor.py").is_file():
    tempd = requests.get("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/Convertor.py")
    with open(Updater + "/Convertor.py", "wb") as f:
        f.write(tempd.content)

if not Path(Updater + "/requirements.txt").is_file():
    tempd = requests.get("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/requirements.txt")
    with open(Updater + "/requirements.txt", "wb") as f:
        f.write(tempd.content)

#Checks for differences
pyresult = filecmp.cmp(python1, python2, shallow=False)
jsonresult = filecmp.cmp(json1, json2, shallow=False)
reqresult = filecmp.cmp(req1, req2, shallow=False)

if jsonresult == False:
    print('Json file is not up to date, updating now...')
    sf = open(json2, "rb")
    tf = open(json1,"wb")
    tf.write(sf.read())
    sf.close()
    tf.close()
    print(Complete)
    jsonresult = filecmp.cmp(json1, json2, shallow=False) #Recheck to make sure the update completed and jsonresult is set to true

if pyresult == False:
    print('Python file is not up to date, updating now...')
    pf = open(python2, "rb")
    kf = open(python1, "wb")
    kf.write(pf.read())
    pf.close()
    kf.close()
    print(Complete)
    pyresult = filecmp.cmp(python1, python2, shallow=False)

if reqresult == False:
    print('Requirements file is not up to date, updating now...')
    uf = open(req2, "rb")
    of = open(req1, "wb")
    of.write(uf.read())
    uf.close()
    of.close()
    print(Complete)
    reqresult = filecmp.cmp(req1, req2, shallow=False)


if pyresult == True and jsonresult == True and reqresult == True:  #After the recheck they all are True and the update is complete
    print('Files are up to date, closing in 10 seconds')
    shutil.rmtree(Updater)
    time.sleep(10)
    quit()