library(IRdisplay)
library(magrittr)
library(tidyverse)
library(scales)
library(gridExtra)
library(forecast)
library(tseries)
library(ggthemes)
library(plyr)



nokia_raw<-read.csv("NOK_2years.csv")
nokia<-na.omit(nokia_raw)
head(nokia);dim(nokia)
class(nokia$Date)
nokia$Date<-as.Date(nokia$Date)
class(nokia$Date)
names(nokia)
names(nokia)[names(nokia)=="Date"]<-"t"
names(nokia)[names(nokia)=="Open"]<-"x"




N1<-ggplot(nokia,aes(x=t,y=x))+geom_line()+xlab("Time")+ylab("Price")+ggtitle("nokia 2-Year Price History")
N2<-ggAcf(nokia$x,type="correlation")+ggtitle("ACF of nokia, 2 years")
N3<-ggAcf(nokia$x,type="partial")+ggtitle("PACF of nokia, 2 years")
grid.arrange(N1,N2,N3)
adf.test(nokia$x)

#fit AR model: auto.arima() function

ar.model<-auto.arima(nokia$x,max.d=0,max.q=0,allowdrift=T)
ar.model

# fit MA model

ma.model<-auto.arima(nokia$x,max.d=0,max.p=0,allowdrift=T)
ma.model

# fit ARMA model

arma.model<-auto.arima(nokia$x,max.d=0,allowdrift=T)
arma.model

# ARIMA

arima.model<-auto.arima(nokia$x,allowdrift=T)
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



# transform data to time series object in R
nokia.ts<-ts(nokia$x,frequency=157)

# fit stl model
stl.model<-stl(nokia.ts,s.window="periodic")

#plot fit
autoplot(stl.model)

# make forecast
decomp.forecast<-forecast(stl.model,h=24,level=65)
autoplot(decomp.forecast)


