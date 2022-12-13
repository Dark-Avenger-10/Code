#Breadth First Seach(BFS)
graph={'A':['B','C','D'],'B':['E','F'],'C':['G','I'],'D':['I'],'E':[],'F':[],'G':[],'H':[],'I':[]}
visited=[]

def BFS(node):
    queue=[]
    queue.append(node)
    visited.append(node)
    
    while queue:
        s=queue.pop(0)
        print(s)
        
        for neighbor in graph[s]:
            if neighbor not in visited:
                visited.append(neighbor)                
                queue.append(neighbor)
print("Breadth First Search of the Graph : ")
BFS('A')

visited=set()
print("Visited :",visited)
def DFS(node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            DFS(neighbor)
print("Depth first Search of the Graph : ")
DFS('A')
