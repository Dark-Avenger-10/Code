#5.1 t-test for single mean
#1)
data=c(12.1,11.9,12.4,12.3,11.5,11.6,12.1,12.4)
t.test(data, mu=12.35,alternative = "two.sided")
# Output : 
#   data:  data
# t = -2.5535, df = 7, p-value = 0.03791
# alternative hypothesis: true mean is not equal to 12.35
# 95 percent confidence interval:
#   11.74811 12.32689
# sample estimates:
#   mean of x 
# 12.0375
#--------------------------------------------------------
#2)
data=c(10.2,9.7,10.1,10.3,10.1,9.8,9.9,10.4,10.3,9.8)
t.test(data, mu=10,alternative = "two.sided")
# Output:
#   One Sample t-test
# data:  data
# t = 0.77174, df = 9, p-value = 0.46
# alternative hypothesis: true mean is not equal to 10
# 95 percent confidence interval:
#   9.884126 10.235874
# sample estimates:
#   mean of x 
# 10.06

#--------------------------------------------------------
#--------------------------------------------------------

#t-test for Two sample test
horseA=c(28,30,32,33,33,29,34)
horseB=c(29,30,30,24,27,29)
t.test(horseA, horseB, mu=0, alternative="two.sided")
# Output:
#   Welch Two Sample t-test
# data:  horseA and horseB
# t = 2.4335, df = 10.652, p-value = 0.03386
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   0.2867853 5.9513100
# sample estimates:
#   mean of x mean of y 
# 31.28571  28.16667

#--------------------------------------------------------
#--------------------------------------------------------

#Paired t-test
A=c(12,14,11,8,7,10,3,0,5,6)
B=c(15,16,10,7,5,12,10,2,3,8)
t.test(A,B,paired = T,alternative = "two.sided"

# Output : 
#   Paired t-test
# 
# data:  A and B
# t = -1.3646, df = 9, p-value = 0.2055
# alternative hypothesis: true mean difference is not equal to 0
# 95 percent confidence interval:
#   -3.1893268  0.7893268
# sample estimates:
#   mean difference 
# -1.2 
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------

#Chi-Square Test
#1)
data=matrix(c(40,20,10,30),2,2,TRUE)
# > data
# [,1] [,2]
# [1,]   40   20
# [2,]   10   30
chisq.test(data)
# Output : 
#   Pearson's Chi-squared test with Yates' continuity correction
# 
# data:  data
# X-squared = 15.042, df = 1, p-value = 0.0001052
#--------------------------------------------------------

#2)
data=matrix(c(460,140,600,40,160,400,700,300,1000),3,3,TRUE)
# > data
# [,1] [,2] [,3]
# [1,]  460  140  600
# [2,]   40  160  400
# [3,]  700  300 1000
chisq.test(data)
# Output : 
#   Pearson's Chi-squared test
# 
# data:  data
# X-squared = 228, df = 4, p-value < 2.2e-16

#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------

#F-test
#1)
horseA=c(28,30,32,33,33,29,34)
horseB=c(29,30,30,24,27,29)

var.test(horseA,horseB,alternative="two.sided")

# Output : 
#   F test to compare two variances
# 
# data:  horseA and horseB
# F = 0.97604, num df = 6, denom df = 5, p-value = 0.9573
# alternative hypothesis: true ratio of variances is not equal to 1
# 95 percent confidence interval:
#   0.1398802 5.8441186
# sample estimates:
#   ratio of variances 
# 0.9760426

#--------------------------------------------------------

#2)
Ea=c(503,505,497,505,419,493,510,501)
Eb=c(502,497,492,490,495,497,596,498)

var.test(Ea,Eb,alternative = "two.sided")

# Output : 
#   F test to compare two variances
# 
# data:  Ea and Eb
# F = 0.70101, num df = 7, denom df = 7, p-value = 0.651
# alternative hypothesis: true ratio of variances is not equal to 1
# 95 percent confidence interval:
#   0.140345 3.501484
# sample estimates:
#   ratio of variances 
# 0.7010104

#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------



