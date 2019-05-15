'''
Anton Kanugalwattage
May 9, 2019
Finding solutions using Euler's Method for Differential Equations
'''

import pylab
from math import *
    
#Getting the function and information from user 
funcInsert = input("Enter the function for dy/dx = f(x,y): (with correct math operations Eg:(2*x*y + x^2)) ")
initialC = input("Enter the inital conditions: \"y(a)=b\" in the form \"a b\" ")
maxX = float(input("Enter final x: "))
h = float(input("Size of step: (lower h = higher accuracy) h = "))

#Extracting info from the inputs
initial = initialC.strip()
initialS = initial.split(" ")
x0,y0 = float(initialS[0]),float(initialS[1])

#Calculating number of steps
N= int((maxX-x0)/h)

#Calculating f(x,y) for a given x and y
def f(funcInsert,x,y):
    funcR1 = funcInsert.replace("x",str(x))
    funcR2=funcR1.replace("y",str(y))
    funcR3=funcR2.replace("^","**")
    return (eval(funcR3))

#Euler's Method
x,y=[x0],[y0]
for i in range(N):
    x.append(x0+h*(i+1))
    y.append(y[i] + h*f(funcInsert,x[i],y[i]))
print("__________________________________________________________________________________________________")
print("Solution using Euler's Method is: ")

#Graphing the solution from Euler's Method
pylab.plot(x,y,)
pylab.title("Solution for dy/dx = " + funcInsert)
pylab.xlabel('x')
pylab.ylabel('y')
pylab.grid()

#Printing Numerical Solutions
print("Solution Table: (x, y)")
print("")
for i in range(len(x)):
    print("    "+str(round(x[i],3))+ "     "+str(round(y[i],3)))

#Outping the graph
pylab.show()
