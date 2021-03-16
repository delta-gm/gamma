import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pandas_datareader as pdr
import statsmodels.api as sm
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime
import os

symbols = [
    {'s':'NXPI','n':'NXP'},
    {'s':'TSLA','n':'TESLA'},
    {'s':'GME','n':'GAMESTOP'},
    {'s':'AAPL','n':'APPLE'},
    {'s':'PLTR','n':'PALANTIR'},
    {'s':'NOK','n':'NOKIA'},
    {'s':'BB','n':'BLACKBERRY'},
    {'s':'ENPH','n':'ENPHASE'},
    {'s':'SPWR','n':'SUNPOWER'},
    {'s':'SUNW','n':'SUNWORKS'},
    {'s':'SOL','n':'RENESOLA'}
]

def formatHeader(symbol,date):
    headerstr = '____________________________\n'
    headerstr += '____{:^20}____\n'.format(symbol)
    headerstr += '____{:^20}____\n'.format(date)
    headerstr += '____________________________\n'

    return headerstr

today = datetime.now()
dateStr = today.strftime('%Y-%m-%d') 
dateTimeStr = today.strftime('%Y-%m-%d %H:%M:%S')

for symbol in symbols:
    data = yf.download(tickers=symbol['s'],period='1d',interval='5m')
    print(formatHeader(symbol['n'],dateTimeStr))
    print(data[0:3])
    print(data[-3:])
    path = os.getcwd() + '\\data\\{}_{}.csv'.format(symbol['s'],dateStr)
    data.to_csv(path,index=True)

