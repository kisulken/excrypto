import os
import sys
import time
import ccxt.async as ccxt

from random import randint
from ccxt_analyzer import DealAnalyzer


def clean_print(*args):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(*args)


def progress(n, p, g1, g2, total):
    if n == 1:
        clean_print(g1.id, "/", g2.id)
    print(n, 'out of', total, '|', p)
    time.sleep(0.05)
    return False  # continue


hitbtc = ccxt.hitbtc()
binance = ccxt.binance()
kucoin = ccxt.kucoin()
poloniex = ccxt.poloniex()
bittrex = ccxt.bittrex()
exmo = ccxt.exmo()
liqui = ccxt.liqui()
gateways = [hitbtc, binance, kucoin, poloniex, bittrex, exmo, liqui]

pairs = ['BCH/USDT', 'BTC/USDT', 'LTC/USDT']
analyzer = DealAnalyzer(gateways)
print('loading markets...')
analyzer.load_markets()
count = 0
try:
    while True:
        count = analyzer.analyze(pairs, progress)
        print("totally added", count, "deals this round. Waiting...")
        time.sleep(randint(60, 120))

except KeyboardInterrupt:
    print('Stopped. Found', count, 'deals')
    sys.exit(0)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
