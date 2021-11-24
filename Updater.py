import requests
import os
import time
import shutil
import filecmp
from os import path, mkdir
from pathlib import Path

Updater = 'Update Resources'

if not path.exists(Updater):
    mkdir(Updater)

if not Path(Updater + "/values.json").is_file():   #If the values.json file does not exist then it creates it
    url = ("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/values.json") #Grabs the values.json file from the github repository
    tempd = requests.get(url)
    with open(Updater + "/values.json", "wb") as f:
        f.write(tempd.content)  #Writes the values.json file

if not Path(Updater + "/Convertor.py").is_file():
    url = ("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/Convertor.py")
    tempd = requests.get(url)
    with open(Updater + "/Convertor.py", "wb") as f:
        f.write(tempd.content)


json1 = 'Resources/values.json'
json2 = 'Update Resources/values.json'
python1 = 'Convertor.py'
python2 = 'Update Resources/Convertor.py'

pyresult = filecmp.cmp(python1, python2, shallow=False)
jsonresult = filecmp.cmp(json1, json2, shallow=False)
print(jsonresult)
print(pyresult)


if jsonresult == False:
    print('Json file is not up to date, updating now...')
    sf = open(json2, "rb")
    tf = open(json1,"wb")
    tf.write(sf.read())
    sf.close()
    tf.close()
    print('Update complete')
    jsonresult = filecmp.cmp(json1, json2, shallow=False)

if pyresult == False:
    print('Python file is not up to date, updating now...')
    pf = open(python2, "rb")
    kf = open(python1, "wb")
    kf.write(pf.read())
    pf.close()
    kf.close()
    print('Update complete')
    pyresult = filecmp.cmp(python1, python2, shallow=False)


if pyresult == True and jsonresult == True:
    print('Files are up to date, closing in 10 seconds')
    shutil.rmtree(Updater)
    time.sleep(10)
    quit()