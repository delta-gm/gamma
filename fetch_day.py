import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import pandas_datareader as pdr
import statsmodels.api as sm
import yfinance as yf
import plotly.graph_objs as go
from datetime import datetime

dateObj = datetime.now()
dateStamp=str(dateObj.year)+'-'+'0'+str(dateObj.month)+'-'+str(dateObj.day)
print(dateStamp)

nxp_data=yf.download(tickers='NXPI',period='1d',interval='5m')
print("___________________________")
print("    ____       NXP       ____    ")
print("    ____   "+ dateStamp +"    ____    ")
print("___________________________")
print(nxp_data[0:3])
print(nxp_data[-3:])
nxp_data.to_csv('C:\\Users\\gmerr\\OneDrive\Documents\\3_10_r_path\\NXP_{date}.csv'.format(date=dateStamp),index=True)

# gme_data=yf.download(tickers='GME',period='1d',interval='5m')
# print("___________________________")
# print("    ____     GAMESTOP     ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(gme_data[0:3])
# print(gme_data[-3:])
# #gme_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\GME_{date}.csv'.format(date=dateStamp),index=True)

# tesla_data=yf.download(tickers='TSLA',period='1d',interval='5m')
# print("___________________________")
# print("    ____       TESLA      ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(tesla_data[0:3])
# print(tesla_data[-3:])
# #tesla_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\TSLA_{date}.csv'.format(date=dateStamp),index=True)

# apple_data=yf.download(tickers='AAPL',period='1d',interval='5m')
# print("___________________________")
# print("    ____       APPLE      ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(apple_data[0:3])
# print(apple_data[-3:])
# #apple_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\AAPL_{date}.csv'.format(date=dateStamp),index=True)

# palantir_data=yf.download(tickers='PLTR',period='1d',interval='5m')
# print("___________________________")
# print("    ____    PALANTIR    ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(palantir_data[0:3])
# print(palantir_data[-3:])
# #palantir_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\PLTR_{date}.csv'.format(date=dateStamp),index=True)

# nokia_data=yf.download(tickers='NOK',period='1d',interval='5m')
# print("___________________________")
# print("    ____      NOKIA      ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(nokia_data[0:3])
# print(nokia_data[-3:])
# #nokia_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\NOK_{date}.csv'.format(date=dateStamp),index=True)

# blackberry_data=yf.download(tickers='BB',period='1d',interval='5m')
# print("___________________________")
# print("    ____    BLACKBERRY    ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(blackberry_data[0:3])
# print(blackberry_data[-3:])
# #blackberry_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\BB_{date}.csv'.format(date=dateStamp),index=True)

# enphase_data=yf.download(tickers='ENPH',period='1d',interval='5m')
# print("___________________________")
# print("    ____     ENPHASE    ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(enphase_data[0:3])
# print(enphase_data[-3:])
# #enphase_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\ENPH_{date}.csv'.format(date=dateStamp),index=True)

# sunpower_data=yf.download(tickers='SPWR',period='1d',interval='5m')
# print("___________________________")
# print("    ____     SUNPOWER    ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(sunpower_data[0:3])
# print(sunpower_data[-3:])
# #sunpower_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\SPWR_{date}.csv'.format(date=dateStamp),index=True)

# sunworks_data=yf.download(tickers='SUNW',period='1d',interval='5m')
# print("___________________________")
# print("    ____     SUNWORKS    ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(sunworks_data[0:3])
# print(sunworks_data[-3:])
# #sunworks_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\SUNW_{date}.csv'.format(date=dateStamp),index=True)

# renesola_data=yf.download(tickers='SOL',period='1d',interval='5m')
# print("___________________________")
# print("    ____    RENESOLA    ____    ")
# print("    ____   "+ dateStamp +"    ____    ")
# print("___________________________")
# print(renesola_data[0:3])
# print(renesola_data[-3:])
# #renesola_data.to_csv(r'C:\Users\gmerr\OneDrive\Documents\3_10_r_path\SOL_{date}.csv'.format(date=dateStamp),index=True)



# # print(NXP_data.head())
# # print(enphase_data.head())
# # print(renesola_data.head())

