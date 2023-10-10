from queue import PriorityQueue
v=14

graph = [[] for i in range(v)]

def BestFirstSearch(source,target,n):
    visited=[False]*n
    pqueue=PriorityQueue()
    pqueue.put((0,source))
    
    visited[source]=True
    
    while pqueue.empty()==False:
        n=pqueue.get()[1]
        print(n,end=' ')

        if n==target:
            break
        for v,h in graph[n]:
            if visited[v]==False:
                visited[v]=True
                pqueue.put((h,v))       
    print()

def addedge(x, y, cost):
    graph[x].append((y, cost))
    graph[y].append((x, cost))
 
 
# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

source=0
target=9

BestFirstSearch(source,target,v)
            
    