
def solveGD(r,x,e):
    iterationcount=0
    previoussize=1
    #functiond =lambda x: 1 - 40*(x)+(9*(x**2))+(4*(x**3))
    #the equation goes above
    check=True
    while(check):
        previousx=x
        x=x-r*functiond(previousx)
        previoussize=abs(previousx-x)
        iterationcount+=1
        if(previoussize<e):
            check=False
            return [round(x,6),iterationcount] 
