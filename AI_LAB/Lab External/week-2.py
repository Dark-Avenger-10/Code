#list opertaions



#Remove duplicate element from the list
n=int(input("Enter no.of elements : "))
print("Enter elements : ",end="")

data=list(map(int,input().split()))
res=[]
data=[res.append(i) for i in data if i not in res]
print("List after removing Duplicates :",res)