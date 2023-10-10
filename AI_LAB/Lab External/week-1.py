#Multiplication Table
n=int(input("Enter a number : "))
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")



#Prime number check
n=int(input("Enter a number to check whether prime or not : "))
if n<2:
    print(n,"is not a Prime Number")
else:
    for i in range(2,(n//2)+1):
        if n%i==0:
            print(n,"Is not a Prime Number")
            break
    else:
        print(n,"Is a prime Number") 
   
   


#Factorial of a Number
n=int(input("Enter a number to find Factorial : "))
fact=1

for i in range(2,n+1):
    fact*=i
print("Factorial of",n,"=",fact)   
