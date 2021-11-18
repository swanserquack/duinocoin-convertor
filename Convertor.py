import requests
import json
import colorama
from colorama import init
from colorama import Fore, Back, Style
init()

response_Duino = requests.get('https://server.duinocoin.com/statistics') #Grabs Data
Duino_Output = response_Duino.text
parse_json = json.loads(Duino_Output) #Turns the API output into a python dictionary and then sets it as the variable parse_json
DuinoPrice = parse_json['Duco price'] #Searches the dictionary for Duco price and sets DuinoPrice to the value

print(Fore.YELLOW + 'Duino Coin Convertor')
print('')
Option = input(Style.RESET_ALL + Fore.CYAN + '1 - Convert from Duino-Coin\n' + Style.RESET_ALL + Fore.GREEN + '2 - Convert to Duino-Coin\n' + Style.RESET_ALL + Fore.MAGENTA + '3 - Quit\n' + Style.RESET_ALL)

def Convert(ID):
    Output = response.text
    parse_json = json.loads(Output) #Turns the API output into a python dictionary and then sets it as the variable parse_json
    Convert.Price = parse_json[ID]['usd'] #Goes through the ID variable then the usd to get the price
    return Convert.Price

if Option == '1':

    Currency=input("What currency do you want to convert to?")

    if Currency.lower() in ('btc', 'bitcoin'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd') #Grabs Data
        ID='bitcoin'
        Convert(ID)
    
    elif Currency.lower() in ('eth', 'ethereum'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
        ID='ethereum'
        Convert(ID)

    elif Currency.lower() in ('ltc', 'litecoin'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        ID='litecoin'
        Convert(ID)
    
    elif Currency.lower() in ('xmr', 'monero'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd')
        ID='monero'
        Convert(ID)
    
    elif Currency.lower() in ('bnb', 'binancecoin'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd')
        ID='binancecoin'
        Convert(ID)

    elif Currency.lower() in ('usdt', 'tether'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd')
        ID='tether'
        Convert(ID)

    elif Currency.lower() in ('ada', 'cardano'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd')
        ID='cardano'
        Convert(ID)

    elif Currency.lower() in ('sol', 'solana'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd')
        ID='solana'
        Convert(ID)

    elif Currency.lower() in ('xrp', 'ripple'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd')
        ID='ripple'
        Convert(ID)

    elif Currency.lower() in ('dot', 'polkadot'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd')
        ID='polkadot'
        Convert(ID)

    elif Currency.lower() in ('usdc', 'usd coin'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=usd')
        ID='usd-coin'
        Convert(ID)

    
    else:
        print("Currency is not currently supported. Open an issue on github to get it added.")
        quit()

    DuinoAmount=float(input("How many Duino-Coins do you have?"))
    DuinoTotal=DuinoPrice*DuinoAmount
    FinalOutput = float(DuinoTotal/float(Convert.Price)) #Floats the CurrencyPrice variable (Due to it being a string on the output) and floats the overall thing.
    print('You would have', FinalOutput ,'amount of', ID)

if Option == '2':

    Currency=input("What currency do you want to convert from?")

    if Currency.lower() in ('btc', 'bitcoin'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd') #Grabs Data
        ID='bitcoin'
        Convert(ID)

    elif Currency.lower() in ('eth', 'ethereum'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
        ID='ethereum'
        Convert(ID)

    elif Currency.lower() in ('ltc', 'litecoin'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
        ID='litecoin'
        Convert(ID)
    
    elif Currency.lower() in ('xmr', 'monero'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd')
        ID='monero'
        Convert(ID)
    
    elif Currency.lower() in ('bnb', 'binancecoin'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd')
        ID='binancecoin'
        Convert(ID)

    elif Currency.lower() in ('usdt', 'tether'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd')
        ID='tether'
        Convert(ID)

    elif Currency.lower() in ('ada', 'cardano'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd')
        ID='cardano'
        Convert(ID)

    elif Currency.lower() in ('sol', 'solana'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd')
        ID='solana'
        Convert(ID)

    elif Currency.lower() in ('xrp', 'ripple'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd')
        ID='ripple'
        Convert(ID)

    elif Currency.lower() in ('dot', 'polkadot'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd')
        ID='polkadot'
        Convert(ID)

    elif Currency.lower() in ('usdc', 'usd coin'):
        response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=usd')
        ID='usd-coin'
        Convert(ID)
    
    else:
        print("Currency is not currently supported. Open an issue on github to get it added")
        quit()

    CoinAmount=float(input("How many coins do you have?"))
    CoinTotal=float(Convert.Price)*CoinAmount
    FinalOutput = float(CoinTotal/DuinoPrice) #Floats the CoinTotal, Divides the CoinTotal by the DuinoPrice and floats it.
    print('You would have', FinalOutput, 'duino-coin')

if Option == '3':
    quit()
