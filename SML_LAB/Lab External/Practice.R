prop.test(x=c(13,18),n=c(110,180),alternative = "two.sided")


A=c(12,14,11,8,7,10,3,0,5,6)
B=c(15,16,10,7,5,12,10,2,3,8)
t.test(A,B,paired = T,alternative = "two.sided")

mf=matrix(c(40,20,10,30),2,2,T)
chisq.test(mf)

iq=matrix(c(400,140,240,160),2,2,T)
chisq.test(iq)

var.test(horseA,horseB,alternative = "two.sided")

#WEEK-6

Diameter=c(18.1,19.6,16.6,16.4,16.9,17.0,20.0,16.6,16.2,18.5,18.7,19.4,17.6,18.3,18.8)
Age=c(44,33,33,32,34,31,33,30,34,34,33,36,33,34,37)
Elevation=c(1.3,2.2,2.2,2.6,2.0,1.8,2.2,3.6,1.6,1.5,2.2,1.7,2.2,1.3,2.6)
Rainfall=c(250,115,75,85,100,75,85,75,225,250,255,175,75,85,90)
Gravity=c(0.63,0.59,0.56,55,0.54,0.59,0.56,0.46,0.63,0.60,0.63,0.58,0.55,0.57,0.62)

mlr=lm(Diameter~Age+Elevation+Rainfall+Gravity)
summary(mlr)

plot(mlr)

predicted=predict(mlr)
resid=residuals(mlr)
dt=matrix(c(Diameter,Age,Elevation,Rainfall,Gravity),15,5)
dt=data.frame(dt)

ggplot(data=dt,aes(x=Age+Elevation+Rainfall+Gravity,y=Diameter))+
        geom_smooth(method = "lm",se=F)+
        geom_segment(aes(xend=Age+Elevation+Rainfall+Gravity,yend=predicted),alpha=.5)+
        geom_point(aes(color=abs(resid),size=10))  

shapiro.test(resid)

install.packages("caTools")
install.packages("car")
install.packages("quantmod")
install.packages("corrplot")

library(caTools)
library(car)
library(quantmod)
library(MASS)
library(corrplot)

data=c(38,30,..........,65,74,.......,61,65,36,35,.........,33,30)
data=matrix(data,nrow = 10,ncol = 3)

data=matrix(c(Diameter,Age,Elevation),15,3)
pca=prcomp(data,scale=T )

kpca=kpca(.,data=data,kernel='rbfdot',features=2)
