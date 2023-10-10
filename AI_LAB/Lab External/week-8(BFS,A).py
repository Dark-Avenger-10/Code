def bfs(mat,stnd,visited,n,heu):
  goal=7
  idx=stnd
  visited[stnd]=True
  print(stnd,"->",end=" ")
  while stnd!=goal:
    """ if stnd==goal:
      break """
    value=2<<31
    for i in range(0,n):
      if mat[stnd][i]!=0 and visited[i]==False:
        if value>int(heu[i]):
          value=int(heu[i])
          idx=i
    stnd=idx
    visited[idx]=True
    if(stnd==goal):
        print(str(idx))
    else:
        print(str(idx)+" ->",end=" ")
  return

mat=[]
temp=[]
"""n=int(input("Enter number od nodes in the graph"))"""
"""for i in range(0,n):
  temp=list(map(int,input().split()))
  mat.append(temp)
"""

mat=[[0 ,11 ,14, 7, 0, 0, 0, 0]
,[11, 0, 0, 0, 15,0,0, 0],
[14, 0, 0, 0, 8, 10, 0, 0],
[7, 0, 0, 0, 0, 25, 0, 0], 
[0, 15, 8, 0, 0, 0, 9, 3],
[0,0,10,25,0,0,0,1],[0,0,0,0,9,0,0,10],[0,0,0,0,0,1,10,0]]
print(mat)
n=8
heu=[]
"""for i in range(0,n):
  heu.append(input("node -> goal = "))"""
heu=[12,13,7,4,9,11,8,0]
print(heu)
visited=[]
for i in range(0,n):
  visited.append(False)
stnd=int(input("Enter the start node : "))
bfs(mat,stnd,visited,n,heu)
#0 11 14 7 0 0 0 0
#11 0 0 0 15 0 0 0
#14 0 0 0 8 10 0 0
#7 0 0 0 0 25 0 0 
#0 15 8 0 0 0 9 0
#1
#1
#0