from collections import defaultdict

jug1,jug2,aim=4,3,2
visited=defaultdict(lambda :False)

def WaterJugsSolver(amt1,amt2):
    if amt1==aim and amt2==0 or amt2==aim and amt1==0:
        print(amt1,amt2)
        return True
    if visited[(amt1,amt2)]==False:
        visited[(amt1,amt2)]=True
        print(amt1,amt2)
        
        return (WaterJugsSolver(0,amt2) or
                WaterJugsSolver(amt1,0) or
                WaterJugsSolver(jug1,amt2) or
                WaterJugsSolver(amt1,jug2) or
                WaterJugsSolver(amt1+min(amt2,jug1-amt1),amt2-min(amt2,jug1-amt1)) or
                WaterJugsSolver(amt1-min(amt1,jug2-amt2),amt2+min(amt1,jug2-amt2))
                ) 
print("Steps : ")
WaterJugsSolver(0,0)