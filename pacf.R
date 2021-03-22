library(isdals)
data(bodyfat)
attach(bodyfat)
pairs(cbind(Fat, Triceps, Thigh, Midarm))
cor(cbind(Fat, Triceps, Thigh, Midarm))


# .hat objects are the linear model predictions of Fat, Triceps on Thigh. 
Fat.hat<-predict(lm(Fat~Thigh))
Triceps.hat<-predict(lm(Triceps~Thigh))

# take the correlation between the difference of each of the two predictors and the components of Thigh in each one. 
cor((Fat-Fat.hat),(Triceps-Triceps.hat))

library(ppcor)
pcor(cbind(Fat,Triceps,Thigh,Midarm))
