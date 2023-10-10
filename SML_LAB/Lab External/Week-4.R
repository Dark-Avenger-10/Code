#Week-4
#Maximum Likelihood Estimation
x=rbinom(100,52,0.6)
mean(x)
phat=mean(x)/52
phat
#Poisson Distribution
x=rpois(100,10)
lambdahat=mean(x)
lambdahat

#Testing of Hypothesis
# 1) A manufacturer of spark plugs clams that 3% of items supplied by him are
# defective. A random sample of 500 plugs is found to have 20 defective items.
# Test the claim of manufacturer.
prop.test(20,500,0.03,alternative = "two.sided")
# 1-sample proportions test with continuity correction
# 
# data:  20 out of 500, null probability 0.03
# X-squared = 1.3918, df = 1, p-value = 0.2381
# alternative hypothesis: true p is not equal to 0.03
# 95 percent confidence interval:
#   0.02524906 0.06216390
# sample estimates:
#   p 
# 0.04 
#--------------No Significant Difference, Ho is Accepted----------------

# 2)We have a population of mice containing half male and have female(p=0.5)
# some of these mice (n=160) have developed a spontaneous cancer, including 95
# male and 65 female. Test whether the cancer affects more male than female
prop.test(x=95,n=160,p=0.5,alternative = "greater")
# 1-sample proportions test with continuity correction
# 
# data:  95 out of 160, null probability 0.5
# X-squared = 5.2562, df = 1, p-value = 0.01093
# alternative hypothesis: true p is greater than 0.5
# 95 percent confidence interval:
#   0.5256923 1.0000000
# sample estimates:
#   p 
# 0.59375
#--------------Significant Difference, Ho is Rejected----------------

#Compare Two Proportions
#1)In a large city A, 20% of a random sample of 900 school children had defective 
# eye sight. In other large city B, 15% of a random sample of 1600 children had
# the same defect. Is this difference between the two proportions significant
prop.test(c(180,240),c(900,1600),alternative = "two.sided")
# 2-sample test for equality of proportions with continuity correction
# 
# data:  c(180, 240) out of c(900, 1600)
# X-squared = 9.9476, df = 1, p-value = 0.001611
# alternative hypothesis: two.sided
# 95 percent confidence interval:
#   0.0176829 0.0823171
# sample estimates:
#   prop 1 prop 2 
# 0.20   0.15
#--------------Significant Difference, Ho is Rejected----------------

#One Sample Z-Test
# 1)Suppose the IQ in a certain population is normally distributed with a mean of
# mu=100 and standard deviation=15. A scientist wants to know if a new medication
# affects IQ levels, so she recruits 20 patients to use it for one month and
# records their IQ levels at the end of the month
z.test(sample(80:120,20),mu=100,sigma.x = 15,alternative = "two.sided")
#One-sample z-Test
# data:  sample(80:120, 20)
# z = 0.52175, p-value = 0.6018
# alternative hypothesis: true mean is not equal to 100
# 95 percent confidence interval:
#   95.17608 108.32392
# sample estimates:
#   mean of x 
# 101.75
#--------------No Significant Difference, Ho is Accepted----------------

#Two Sample Z-test
# 1) Suppose the IQ Levels among individuals in two different cities are known to
# be normally distributed each with a standard deviations of 15. A scientist wants
# to know if the mean IQ level between individuals in city A and City B are differ
# ent, so she selects a simple random sample of 20 individuals from each city and 
# records their IQ Levels.
cityA=rnorm(n=20,sd=15)
cityB=rnorm(n=20,sd=15)

z.test(x=cityA,y=cityB,alternative = "two.sided",sigma.x=15,sigma.y=15)

# Two-sample z-Test
# 
# data:  cityA and cityB
# z = 0.61338, p-value = 0.5396
# alternative hypothesis: true difference in means is not equal to 0
# 95 percent confidence interval:
#   -6.387411 12.206440
# sample estimates:
#   mean of x mean of y 
# -1.722722 -4.632236
#--------------No Significant Difference, Ho is Accepted----------------





