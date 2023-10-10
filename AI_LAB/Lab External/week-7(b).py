from ortools.sat.python import cp_model
model=cp_model.CpModel()

t=model.NewIntVar(1,9,'T')
w=model.NewIntVar(0,9,'W')
o=model.NewIntVar(0,9,'O')

f=model.NewIntVar(1,9,'F')
u=model.NewIntVar(0,9,'U')
r=model.NewIntVar(0,9,'R')

    
letters=[w,o,f,u,t,r]

model.AddAllDifferent(letters)
#CP + IS + FUN = TRUE
model.Add(t*100 + w*10 + o + t*100 + w*10 + o == f*1000 + o*100 + u*10 + r)

class VarArraySolutionPrinter(cp_model.CpSolverSolutionCallback):
    def __init__(self,variables):
        cp_model.CpSolverSolutionCallback.__init__(self)
        self.__variables=variables
        self.__solution_count=0
    
    def on_solution_callback(self):
        self.__solution_count+=1
        for v in self.__variables:
            print('%s=%i' %(v,self.Value(v)),end=' ')
        print()
    def solution_count(self):
        return self.__solution_count

solver=cp_model.CpSolver()
solution_printer=VarArraySolutionPrinter(letters)
status = solver.SearchForAllSolutions(model,solution_printer)
print("No.of Solutions :",solution_printer.solution_count())