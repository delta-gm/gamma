import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pandas_datareader as pdr
import statsmodels.api as sm
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime

# This should be used to initialize the R models. Each ticker will need AR, MA, ARMA, ARIMA models
# compared for residuals and fit. Once the histories of all these tickers have been fitted in a model, 
# the model should be fed data from fetch_day.py. 

# dateObj = datetime.now()
# dateStamp=str(dateObj.year)+'-'+'0'+str(dateObj.month)+'-'+str(dateObj.day)
# print(dateStamp)

nxp_data=yf.download(tickers='NXPI',period='2y',interval='1d')
nxp_data.to_csv(r'C:\repos\GammaWar\NXP_2years.csv',index=True)

gme_data=yf.download(tickers='GME',period='2y',interval='1d')
gme_data.to_csv(r'C:\repos\GammaWar\GME_2years.csv',index=True)

tesla_data=yf.download(tickers='TSLA',period='2y',interval='1d')
tesla_data.to_csv(r'C:\repos\GammaWar\TSLA_2years.csv',index=True)

apple_data=yf.download(tickers='AAPL',period='2y',interval='1d')
apple_data.to_csv(r'C:\repos\GammaWar\AAPL_2years.csv',index=True)

palantir_data=yf.download(tickers='PLTR',period='2y',interval='1d')
palantir_data.to_csv(r'C:\repos\GammaWar\PLTR_2years.csv',index=True)

nokia_data=yf.download(tickers='NOK',period='2y',interval='1d')
nokia_data.to_csv(r'C:\repos\GammaWar\NOK_2years.csv',index=True)

blackberry_data=yf.download(tickers='BB',period='2y',interval='1d')
blackberry_data.to_csv(r'C:\repos\GammaWar\BB_2years.csv',index=True)

enphase_data=yf.download(tickers='ENPH',period='2y',interval='1d')
enphase_data.to_csv(r'C:\repos\GammaWar\ENPH_2years.csv',index=True)

sunpower_data=yf.download(tickers='SPWR',period='2y',interval='1d')
sunpower_data.to_csv(r'C:\repos\GammaWar\SPWR_2years.csv',index=True)

sunworks_data=yf.download(tickers='SUNW',period='2y',interval='1d')
sunworks_data.to_csv(r'C:\repos\GammaWar\SUNW_2years.csv',index=True)

renesola_data=yf.download(tickers='SOL',period='2y',interval='1d')
renesola_data.to_csv(r'C:\repos\GammaWar\SOL_2years.csv',index=True)



print(NXP_data.head())
print(enphase_data.head())
print(renesola_data.head())

