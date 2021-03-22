library(IRdisplay)
library(magrittr)
library(tidyverse)
library(scales)
library(gridExtra)
library(forecast)
library(tseries)
library(ggthemes)
library(plyr)



enphase_raw<-read.csv("ENPH_2years.csv")
enphase<-na.omit(enphase_raw)
head(enphase);dim(enphase)
class(enphase$Date)
enphase$Date<-as.Date(enphase$Date)
class(enphase$Date)
names(enphase)
names(enphase)[names(enphase)=="Date"]<-"t"
names(enphase)[names(enphase)=="Open"]<-"x"


N1<-ggplot(enphase,aes(x=t,y=x))+geom_line()+xlab("Time")+ylab("Price")+ggtitle("enphase 2-Year Price History")
N2<-ggAcf(enphase$x,type="correlation")+ggtitle("ACF of enphase, 2 years")
N3<-ggAcf(enphase$x,type="partial")+ggtitle("PACF of enphase, 2 years")
grid.arrange(N1,N2,N3)
adf.test(enphase$x)

# STL Decomposition Models

# Loess regression - local linear regression that applies more weight to data closer in time
# to point of estimation. 

# STL models use two loops: inner computes trend and seasonal components w/loess
# Outer loop computes residuals
# Loops run until convergence 

# transform data to time series object in R
enphase.ts<-ts(enphase$x,frequency=12)

# fit stl model
stl.model<-stl(enphase.ts,s.window="periodic")

#plot fit
autoplot(stl.model)

# make forecast
decomp.forecast<-forecast(stl.model,h=24,level=95)
autoplot(decomp.forecast)

#fit AR model: auto.arima() function

ar.model<-auto.arima(enphase$x,max.d=0,max.q=0,allowdrift=T)
ar.model

# fit MA model

ma.model<-auto.arima(enphase$x,max.d=0,max.p=0,allowdrift=T)
ma.model

# fit ARMA model

arma.model<-auto.arima(enphase$x,max.d=0,allowdrift=T)
arma.model

# ARIMA

arima.model<-auto.arima(enphase$x,allowdrift=T)
arima.model

# Ljung box test: null hypothesis of white noise - want to fail to reject this
# check resids to make sure they are white noise

ar.residual<-resid(ar.model)
ma.residual<-resid(ma.model)
arma.residual<-resid(arma.model)
arima.residual<-resid(arima.model)

# plot pacf of each model's resids

ar_pacf<-ggAcf(ar.residual,type="partial")
ma_pacf<-ggAcf(ma.residual,type="partial")
arma_pacf<-ggAcf(arma.residual,type="partial")
arima_pacf<-ggAcf(arima.residual,type="partial")
grid.arrange(ar_pacf,ma_pacf,arma_pacf,arima_pacf)


# box.test() for ljung box test - specify both test type and number of lags to test

Box.test(ar.residual,type="Ljung-Box",lag=1)
Box.test(ma.residual,type="Ljung-Box",lag=1)
Box.test(arma.residual,type="Ljung-Box",lag=1)
Box.test(arima.residual,type="Ljung-Box",lag=1)

# when p-value is > 0.05, rejection of null hypothesis fails. So we don't have to worry 
# about stationarity with these models and we can forecast.

ar.forecast<-forecast(ar.model,h=24,level=80)
ma.forecast<-forecast(ma.model,h=24,level=80)
arma.forecast<-forecast(arma.model,h=24,level=80)
arima.forecast<-forecast(arima.model,h=24,level=80)

# plot forecast - autoplot()

ar_cast<-autoplot(ar.forecast)
ma_cast<-autoplot(ma.forecast)
arma_cast<-autoplot(arma.forecast)
arima_cast<-autoplot(arima.forecast)
grid.arrange(ar_cast,ma_cast,arma_cast,arima_cast)


# STL Decomposition Models

# Loess regression - local linear regression that applies more weight to data closer in time
# to point of estimation. 

# STL models use two loops: inner computes trend and seasonal components w/loess
# Outer loop computes residuals
# Loops run until convergence 

# transform data to time series object in R
enphase.ts<-ts(enphase$x,frequency=200)

# fit stl model
stl.model<-stl(enphase.ts,s.window="periodic")

#plot fit
autoplot(stl.model)

# make forecast
decomp.forecast<-forecast(stl.model,h=12,level=95)
autoplot(decomp.forecast)


