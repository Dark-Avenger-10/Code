# Multiple Linear Regression Analysis
Diameter=c(18.1,19.6,16.6,16.4,16.9,17.0,20.0,16.6,16.2,18.5,18.7,19.4,17.6,18.3,18.8)
Age=c(44,33,33,32,34,31,33,30,34,34,33,36,33,34,37)
Elevation=c(1.3,2.2,2.2,2.6,2.0,1.8,2.2,3.6,1.6,1.5,2.2,1.7,2.2,1.3,2.6)
Rainfall=c(250,115,75,85,100,75,85,75,225,250,255,175,75,85,90)
Gravity=c(0.63,0.59,0.56,55,0.54,0.59,0.56,0.46,0.63,0.60,0.63,0.58,0.55,0.57,0.62)

mlr=lm(Diameter~Age)
summary(mlr)

ggplot(mlr,aes(x=.fitted, y=.resid)) + geom_point() + geom_hline(yintercept = 0)

plot(mlr,2)
shapiro.test(res)