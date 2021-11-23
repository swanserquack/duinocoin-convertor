import requests
import json
import colorama
import os
import filecmp
from json import load
from os import path, mkdir
from pathlib import Path
from colorama import init
from colorama import Fore, Back, Style
init()

Folder = 'Resources'
f1 = "Convertor.py"
f2 = "Resources/Updater.py"

if not path.exists(Folder):
    mkdir(Folder)  #If the Resource folder does not exist then it creates it

if not Path(Folder + "/values.json").is_file():   #If the values.json file does not exist then it creates it
    url = ("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/values.json") #Grabs the values.json file from the github repository
    tempd = requests.get(url)
    with open(Folder + "/values.json", "wb") as f:
        f.write(tempd.content)  #Writes the values.json file

url = ("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/Convertor.py") #Grabs the values.json file from the github repository
tempd = requests.get(url)
with open(Folder + "/Updater.py", "wb") as f:
    f.write(tempd.content)  #Writes the Convertors

with open(Folder + "/values.json", "r", encoding='utf-8') as values:
    values = load(values) #Loads it


request = requests.get("https://raw.githubusercontent.com/swanserquack/duinocoin-convertor/main/Convertor.py")

result = filecmp.cmp(f1, f2, shallow=False)

if result == True:
    print('Version Up To Date')

elif result == False:
    with open("Convertor.py", "wb") as f1:
        str(request.content)
        f1.write(request.content)
        print('Update Complete')
        quit()

response_Duino = requests.get('https://server.duinocoin.com/statistics') #Grabs Data
Duino_Output = response_Duino.text
parse_json = json.loads(Duino_Output) #Turns the API output into a python dictionary and then sets it as the variable parse_json
DuinoPrice = parse_json['Duco price'] #Searches the dictionary for Duco price and sets DuinoPrice to the value

def Convert(ID):
    Output = response.text
    parse_json = json.loads(Output) #Turns the API output into a python dictionary and then sets it as the variable parse_json
    Convert.Price = parse_json[ID]['usd'] #Goes through the ID variable then the usd to get the price
    return Convert.Price

def CalculationTo(ID):
    DuinoAmount=float(input("How many Duino-Coins do you have?"))
    DuinoTotal=DuinoPrice*DuinoAmount
    FinalOutput = float(DuinoTotal/float(Convert.Price)) #Floats the CurrencyPrice variable (Due to it being a string on the output) and floats the overall thing.
    print('You would have', FinalOutput ,'amount of', ID)

def CalculationFrom():
    CoinAmount=float(input("How many coins do you have?"))
    CoinTotal=float(Convert.Price)*CoinAmount
    FinalOutput = float(CoinTotal/DuinoPrice) #Floats the CoinTotal, Divides the CoinTotal by the DuinoPrice and floats it.
    print('You would have', FinalOutput, 'duino-coin')

def NoSupport():
    print("Currency is not currently supported. Open an issue on github to get it added.")
    quit()

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