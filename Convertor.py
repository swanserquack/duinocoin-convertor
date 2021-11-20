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



if Option == '1':

    Currency=input("What currency do you want to convert to?").lower()

    if Currency.startswith('a'):

        if Currency in ('ada'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd')
            ID='cardano'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('atom'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cosmos=&vs_currencies=usd')
            ID='cosmos'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('b'):

        if Currency in ('btc', 'bitcoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd') #Grabs Data
            ID='bitcoin'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('bnb', 'binancecoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd')
            ID='binancecoin'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('bch', 'bitcoincash', 'bitcoin cash'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin-cash&vs_currencies=usd')
            ID='bitcoin-cash'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('bat', 'basicattentiontoken', 'basic attention token'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=basic-attention-token&vs_currencies=usd')
            ID='basic-attention-token'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('beam'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=beam&vs_currencies=usd')
            ID='beam'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('c'):
        
        if Currency in ('cardano'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd')
            ID='cardano'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('chia'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chia&vs_currencies=usd')
            ID='chia'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('cake'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=pancakeswap-token&vs_currencies=usd')
            ID='pancakeswap-token'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('cosmos'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cosmos=&vs_currencies=usd')
            ID='cosmos'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('chainlink'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chainlink&vs_currencies=usd')
            ID='chainlink'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()
    
    if Currency.startswith('d'):

        if Currency in ('dot'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd')
            ID='polkadot'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('doge', 'dogecoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd')
            ID='dogecoin'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('dash'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=dash&vs_currencies=usd')
            ID='dash'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('dgb', 'digibyte'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=digibyte&vs_currencies=usd')
            ID='digibyte'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()
    
    if Currency.startswith('e'):

        if Currency in ('eth', 'ethereum'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
            ID='ethereum'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('etc', 'ethereumclassic', 'ethereum classic'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum-classic&vs_currencies=usd')
            ID='ethereum-classic'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('eos'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=eos&vs_currencies=usd')
            ID='eos'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('enj', 'enjincoin', 'enjin coin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=enjincoin&vs_currencies=usd')
            ID='enjincoin'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('f'):

        if Currency in ('fil', 'filecoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=filecoin&vs_currencies=usd')
            ID='filecoin'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('h'):

        if Currency in ('hnt', 'helium'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=helium&vs_currencies=usd')
            ID='helium'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('l'):

        if Currency in ('ltc', 'litecoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
            ID='litecoin'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('link'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chainlink&vs_currencies=usd')
            ID='chainlink'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('m'):

        if Currency in ('monero'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd')
            ID='monero'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('n'):

        if Currency in ('neo'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=neo&vs_currencies=usd')
            ID='neo'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('nexo'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=nexo&vs_currencies=usd')
            ID='nexo'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('p'):

        if Currency in ('polkadot'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd')
            ID='polkadot'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('pancakeswap', 'pancake swap'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=pancakeswap-token&vs_currencies=usd')
            ID='pancakeswap-token'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('r'):

        if Currency in ('ripple'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd')
            ID='ripple'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('rvn', 'ravencoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ravencoin&vs_currencies=usd')
            ID='ravencoin'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('s'):

        if Currency in ('sol', 'solana'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd')
            ID='solana'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('storj'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=storj&vs_currencies=usd')
            ID='storj'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('stellar'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=stellar&vs_currencies=usd')
            ID='stellar'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('shib', 'shibainu', 'shiba inu'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=usd')
            ID='shiba-inu'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('t'):

        if Currency in ('tether'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd')
            ID='tether'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('trx', 'tron'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd')
            ID='tron'
            Convert(ID)
            CalculationTo(ID)


        elif Currency in ('theta'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=theta-token&vs_currencies=usd')
            ID='theta-token'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()

    if Currency.startswith('u'):
        
        if Currency in ('usdt'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd')
            ID='tether'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('usdc', 'usd coin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=usd')
            ID='usd-coin'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()
    
    if Currency.startswith('x'):

        if Currency in ('xmr'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd')
            ID='monero'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('xrp'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd')
            ID='ripple'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('xch'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chia&vs_currencies=usd')
            ID='chia'
            Convert(ID)
            CalculationTo(ID)

        elif Currency in ('xlm'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=stellar&vs_currencies=usd')
            ID='stellar'
            Convert(ID)
            CalculationTo(ID)

        else:
            NoSupport()
    
    if Currency.startswith('z'):

        if Currency in ('zec', 'zcash'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=zcash&vs_currencies=usd')
            ID='zcash'
            Convert(ID) 
            CalculationTo(ID) 

        else:
            NoSupport()  


if Option == '2':

    Currency=input("What currency do you want to convert from?").lower()

    if Currency.startswith('a'):

        if Currency in ('ada'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd')
            ID='cardano'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('atom'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cosmos=&vs_currencies=usd')
            ID='cosmos'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('b'):

        if Currency in ('btc', 'bitcoin', 'BTC'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd') #Grabs Data
            ID='bitcoin'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('bnb', 'binancecoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=binancecoin&vs_currencies=usd')
            ID='binancecoin'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('bch', 'bitcoincash', 'bitcoin cash'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin-cash&vs_currencies=usd')
            ID='bitcoin-cash'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('bat', 'basicattentiontoken', 'basic attention token'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=basic-attention-token&vs_currencies=usd')
            ID='basic-attention-token'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('beam'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=beam&vs_currencies=usd')
            ID='beam'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('c'):
        
        if Currency in ('cardano'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd')
            ID='cardano'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('chia'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chia&vs_currencies=usd')
            ID='chia'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('cake'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=pancakeswap-token&vs_currencies=usd')
            ID='pancakeswap-token'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('cosmos'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=cosmos=&vs_currencies=usd')
            ID='cosmos'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('chainlink'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chainlink&vs_currencies=usd')
            ID='chainlink'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()
    
    if Currency.startswith('d'):

        if Currency in ('dot'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd')
            ID='polkadot'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('doge', 'dogecoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd')
            ID='dogecoin'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('dash'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=dash&vs_currencies=usd')
            ID='dash'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('dgb', 'digibyte'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=digibyte&vs_currencies=usd')
            ID='digibyte'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()
    
    if Currency.startswith('e'):

        if Currency in ('eth', 'ethereum'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
            ID='ethereum'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('etc', 'ethereumclassic', 'ethereum classic'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum-classic&vs_currencies=usd')
            ID='ethereum-classic'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('eos'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=eos&vs_currencies=usd')
            ID='eos'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('enj', 'enjincoin', 'enjin coin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=enjincoin&vs_currencies=usd')
            ID='enjincoin'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('f'):

        if Currency in ('fil', 'filecoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=filecoin&vs_currencies=usd')
            ID='filecoin'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('h'):

        if Currency in ('hnt', 'helium'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=helium&vs_currencies=usd')
            ID='helium'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('l'):

        if Currency in ('ltc', 'litecoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')
            ID='litecoin'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('link'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chainlink&vs_currencies=usd')
            ID='chainlink'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('m'):

        if Currency in ('monero'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd')
            ID='monero'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('n'):

        if Currency in ('neo'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=neo&vs_currencies=usd')
            ID='neo'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('nexo'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=nexo&vs_currencies=usd')
            ID='nexo'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('p'):

        if Currency in ('polkadot'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=polkadot&vs_currencies=usd')
            ID='polkadot'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('pancakeswap', 'pancake swap'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=pancakeswap-token&vs_currencies=usd')
            ID='pancakeswap-token'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('r'):

        if Currency in ('ripple'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd')
            ID='ripple'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('rvn', 'ravencoin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ravencoin&vs_currencies=usd')
            ID='ravencoin'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('s'):

        if Currency in ('sol', 'solana'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=solana&vs_currencies=usd')
            ID='solana'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('storj'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=storj&vs_currencies=usd')
            ID='storj'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('stellar'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=stellar&vs_currencies=usd')
            ID='stellar'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('shib', 'shibainu', 'shiba inu'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=shiba-inu&vs_currencies=usd')
            ID='shiba-inu'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('t'):

        if Currency in ('tether'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd')
            ID='tether'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('trx', 'tron'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tron&vs_currencies=usd')
            ID='tron'
            Convert(ID)
            CalculationFrom()


        elif Currency in ('theta'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=theta-token&vs_currencies=usd')
            ID='theta-token'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()

    if Currency.startswith('u'):
        
        if Currency in ('usdt'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=tether&vs_currencies=usd')
            ID='tether'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('usdc', 'usd coin'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=usd-coin&vs_currencies=usd')
            ID='usd-coin'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()
    
    if Currency.startswith('x'):

        if Currency in ('xmr'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=monero&vs_currencies=usd')
            ID='monero'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('xrp'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ripple&vs_currencies=usd')
            ID='ripple'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('xch'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=chia&vs_currencies=usd')
            ID='chia'
            Convert(ID)
            CalculationFrom()

        elif Currency in ('xlm'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=stellar&vs_currencies=usd')
            ID='stellar'
            Convert(ID)
            CalculationFrom()

        else:
            NoSupport()
    
    if Currency.startswith('z'):

        if Currency in ('zec', 'zcash'):
            response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=zcash&vs_currencies=usd')
            ID='zcash'
            Convert(ID) 
            CalculationFrom()
        
        else:
            NoSupport()
    

if Option == '3':
    quit()
