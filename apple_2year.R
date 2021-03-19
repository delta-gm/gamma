apple<-read.csv("AAPL_2years.csv",header=TRUE)
apple.ts<-ts(apple[,2])

plot(apple.ts,ylab='price',main='apple Price Data')
apple.MA<-filter(apple.ts,rep(1/31,31),sides=2)
lines(apple.MA,col='red')


par(mfrow=c(3,1))
y<-apple.ts/apple.MA
plot(y,ylab='scaled price',main='Transformed apple Price Data')
acf(na.omit(y),main='Autocorrelation Function of Transformed apple Data')
acf(na.omit(y), type='partial',main='Partial ACF of Transformed apple Data')

# apple.MA<-apple.MA
par(mfrow=c(3,1))
plot(apple.MA,ylab='apple ma price',main='apple MA data')
plot(apple.ts,ylab='price',main='apple Price Data')
acf(na.omit(apple.MA),main='ACF of apple MA')
acf(na.omit(apple.MA),type='partial',main='PACF of apple MA')
