import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pandas_datareader as pdr
import statsmodels.api as sm
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime
import os

# This should be used to initialize the R models. Each ticker will need AR, MA, ARMA, ARIMA models
# compared for residuals and fit. Once the histories of all these tickers have been fitted in a model, 
# the model should be fed data from fetch_day.py. 

PERIOD = '2y'
INTERVAL = '1d'

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

for symbol in symbols:
    filepath = os.getcwd() + '\\{}_{}.csv'.format(symbol['s'],PERIOD)
    data = yf.download(tickers=symbol['s'],period=PERIOD,interval=INTERVAL)
    data.to_csv(filepath,index=True)
