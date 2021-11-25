#!/usr/bin/env python3
##########################################
# Duino-Coin Convertor
# https://github.com/swanserquack/duinocoin-convertor
# No copyright
##########################################

import requests
import colorama
import ujson
import filecmp
import os
import shutil
from os import path, mkdir
from pathlib import Path
from colorama import init
from colorama import Fore, Back, Style
init()

Folder = 'Resources'
Updater = 'Update Resources'
Updater1 = 'Update Resources/Updater.py'
Updater2 = 'Updater.py'


if not path.exists(Updater):
    mkdir(Updater)

if not Path(Updater + "/Updater.py").is_file(): #Same here as above
    tempd = requests.get("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/Updater.py")
    with open(Updater + "/Updater.py", "wb") as f:
        f.write(tempd.content)

updateresult = filecmp.cmp(Updater1, Updater2, shallow=False)

if updateresult == False:
    sf = open(Updater1, "rb")
    tf = open(Updater2,"wb")
    tf.write(sf.read())
    sf.close()
    tf.close()
    shutil.rmtree(Updater)

if updateresult == True:
    shutil.rmtree(Updater)

if not path.exists(Folder):
    mkdir(Folder)  #If the Resource folder does not exist then it creates it

if not Path(Folder + "/values.json").is_file():   #If the values.json file does not exist then it creates it
    tempd = requests.get("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/Resources/values.json")
    with open(Folder + "/values.json", "wb") as f:
        f.write(tempd.content)  #Writes the values.json file

with open(Folder + "/values.json", "r", encoding='utf-8') as values:
    values = ujson.load(values) #Loads it


response_Duino = requests.get('https://server.duinocoin.com/statistics') #Grabs Data
Duino_Output = response_Duino.text
parse_json = ujson.loads(Duino_Output) #Turns the API output into a python dictionary and then sets it as the variable parse_json
DuinoPrice = parse_json['Duco price'] #Searches the dictionary for Duco price and sets DuinoPrice to the value


def Convert(ID):
    Output = response.text
    parse_json = ujson.loads(Output) #Turns the API output into a python dictionary and then sets it as the variable parse_json
    Convert.Price = parse_json[ID]['usd'] #Goes through the ID variable then the usd to get the price
    return Convert.Price

def CalculationTo(ID):
    DuinoAmount=float(input("How many Duino-Coins do you have?"))
    DuinoTotal=DuinoPrice*DuinoAmount
    FinalOutput = float(DuinoTotal/float(Convert.Price)) #Floats the CurrencyPrice variable (Due to it being a string on the output) and floats the overall thing.
    print('You would have', FinalOutput ,'amount of', ID, '\n')
        

def CalculationFrom():
    CoinAmount=float(input("How many coins do you have?"))
    CoinTotal=float(Convert.Price)*CoinAmount
    FinalOutput = float(CoinTotal/DuinoPrice) #Floats the CoinTotal, Divides the CoinTotal by the DuinoPrice and floats it.
    print('You would have', FinalOutput, 'duino-coin\n')

def NoSupport():
    print("Currency is not currently supported. Open an issue on github to get it added.")
    quit()


while True:
    print(Fore.YELLOW + 'Duino Coin Convertor')
    print('')
    Option = input(Style.RESET_ALL + Fore.CYAN + '1 - Convert from Duino-Coin\n' + Style.RESET_ALL + Fore.GREEN + '2 - Convert to Duino-Coin\n' + Style.RESET_ALL + Fore.MAGENTA + '3 - Quit\n' + Style.RESET_ALL)

    if Option == '1':
        Currency=input("What currency do you want to convert to?")

        for option in values["currency_options"]:
            if Currency.lower() in option['names']:
                ID = option['id']
                URL = option['url']
                response = requests.get(URL)
                Convert(ID)
                CalculationTo(ID)
                break  
        else:
            NoSupport()

    elif Option == '2':
        Currency=input("What currency do you want to convert from?")
        
        for option in values["currency_options"]:
            if Currency.lower() in option['names']:
                ID = option['id']
                URL = option['url']
                response = requests.get(URL)
                Convert(ID)
                CalculationFrom()
                break
        else:
            NoSupport()
            
    elif Option == '3':
        quit()