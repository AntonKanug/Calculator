'''
Anton Kanugalwattage
May 4, 2019
Calculator for ploynomials, Overview:
- Derivative, Slope at a point
- Integral, Definite Integral
- Graphing
'''

import pylab
from math import *
from fractions import Fraction
###Getting the function from user 
    
#Scanning the function
func = input("Enter the function each separated by a space: (Eg: ax^n + cx^m + b)")
    
#Taking the function and creating a list of coeff and exponents
funcS = func.split(" ")
y,x=[],[]
for i in range(len(funcS)):
    if funcS[i]!= " ":
        y.append(funcS[i])
coeffList, powerList = [],[]    

for i in range(len(y)):
    x.append(y[i].split("x"))
    
    if len(x[i])==2 and i==0 and x[i][1]=="" and x[i][0]=="":
        coeffList.append(1)
        powerList.append(1)
        
    elif len(x[i])==2 and i==0 and x[i][1]=="":
        coeffList.append((x[i][0]))
        powerList.append(1)
        
    elif len(x[i])==1 and i==0:
        coeffList.append((x[i][0]))
        powerList.append("0")
    
    elif i==0 and len(x[i])==2 and len(x[i][0])!=0:
        coeffList.append((x[i][0][0:]))
        powerList.append(x[i][1][1:])

    elif i==0 and len(x[i])==2:
        coeffList.append("1")
        powerList.append(x[i][1][1:])

    elif i==0 and len(x[i])==1:
        coeffList.append((x[i][0][:-1]))
    
    elif len(x[i])==2 and i%2==0 and x[i][1]=="" and x[i][0]=="":
        coeffList.append(x[i-1][0]+"1")
        powerList.append(1)

    elif len(x[i])==2 and i%2==0 and x[i][1]=="":
        coeffList.append(x[i-1][0]+(x[i][0]))
        powerList.append(1)

    elif len(x[i])==2 and i%2==0:
        coeffList.append(x[i-1][0]+(x[i][0]))
        powerList.append(x[i][1][1:])

    elif len(x[i])==1 and i%2==0:
        coeffList.append(x[i-1][0]+(x[i][0]))
        powerList.append("0")
        
#Finding the Derivative and Integral functions
derivExpList , intExpList, derivCoeff, intCoeff = [], [], [], []
for i in range(len(coeffList)):
    derivExpList.append(float(powerList[i])-1)
    intExpList.append(float(powerList[i])+1)
    derivCoeff.append(float(coeffList[i])*float(powerList[i]))
    if intExpList[i] == 0:
        intCoeff.append(float(coeffList[i]))
    else:
        intCoeff.append(float(coeffList[i])/float(intExpList[i]))

        

##Printing the function
print("__________________________________________________________________________________________________")
print("Function is; f(x) = "+func)
##Printing the Derivative function
print("__________________________________________________________________________________________________")
#Removing the 0 coeff case
derivCoeffUP,derivExpListUP=[], []
for i in range(len(derivCoeff)):
    if derivCoeff[i]!=0:
        derivCoeffUP.append(derivCoeff[i])
        derivExpListUP.append(derivExpList[i])

print("First Deravitive is; f'(x) = ", end = "")
z=0
for i in range(len(derivCoeffUP)):
    if z < len(derivCoeffUP)-1:
        if derivExpListUP[i]==1.0:
            print(str(derivCoeffUP[i])+"x" ,end=" + ")
        elif derivExpListUP[i]==0 and derivCoeffUP[i] !=0 and derivExpListUP[i]!=-1:
            print(derivCoeffUP[i], end=" + ")
        elif derivCoeffUP[i] !=0 and derivExpList[i] !=-1:
            print(str(derivCoeffUP[i])+"x^"+str(derivExpListUP[i]) ,end=" + ")
    z+=1
    
#Printing the last part of the polynomial to avoid "+" at the end
if derivExpListUP[-1]==0 and derivCoeffUP[-1] !=0:
    print(derivCoeffUP[-1])
elif derivExpListUP[-1]==1.0:
    print(str(derivCoeffUP[i])+"x")
elif derivCoeffUP[-1] !=0:
    print(str(derivCoeffUP[-1])+ "x^" + str(derivExpListUP[-1]))

    
##Printing the Integral function
print("__________________________________________________________________________________________________")
z=0
print("Integral is; F(x) = ", end = "")
for i in range(len(intCoeff)):
    if intExpList[i]==1.0:
        print(str(intCoeff[i])+"x" ,end=" + ")
    elif intCoeff[i]!=0.0 and intExpList[i]!=0.0:
        print(str(intCoeff[i])+"x^"+str(intExpList[i]) ,end=" + ")
    elif intExpList[i]==0.0:
        print(str(intCoeff[i])+ "ln|x|" ,end=" + ")
print("C")



###Calculating values from the given function
def f(x):
    y =0
    for i in range(len(coeffList)):
        y += float(coeffList[i])*(x**(float(powerList[i])))       
    return y


###Calculating values from the derivative function
def deriv(x):
    m =0
    for i in range(len(derivCoeffUP)):
        m += float(derivCoeffUP[i])*(x**(float(derivExpListUP[i])))       
    return m


###Calculating values from the integral function
def integral(x):
    a =0
    for i in range(len(intCoeff)):
        if intExpList[i]==0:
            a += float(intCoeff[i])*(log(abs(x),e)) 
        else:
            a += float(intCoeff[i])*(x**(float(intExpList[i])))       
    return a
    
    
###while loop till the user is finished with the operations
done = " "
while done != "":
    
    #Asking user for what calculator is to be used
    print("__________________________________________________________________________________________________")
    print("For Derivative Calculator enter \"1\":\nFor Definite Integral enter \"2\":")
    print("For a graph of the function enter \"3\": (Warning the program must be terminated for graphing to execute)")
    print("To end the program press \"Enter\" :")
    insertCal = input("")
    
    #To End Program
    if insertCal == "":
        break
        
    ##Slope Calculator
    elif insertCal == "1":
        print("__________________________________________________________________________________________________")
        x = float(input("Enter the x value:"))    
        m = deriv(x)
        print("__________________________________________________________________________________________________")
        print("\nThe slope at the point (" + str(x) + "," +str(f(x)) +") is " + str(Fraction(m)) + " or " + str(m))
    
    
    ##Definite Integral
    elif insertCal == "2":
        
        #Asking user for the interval
        print("__________________________________________________________________________________________________")
        intervalInput = input("Enter an interval that f(x) is continuous to find the area: (seperated by a space)")
        intervalInt = intervalInput.split(" ")
        x1, x2 = float(intervalInt[0]), float(intervalInt[1])
        
        #Using the integral function that was derived
        area = integral(x2)-integral(x1)
        
        print("__________________________________________________________________________________________________")
        print("The area on the interval [" + str(x1) + ","+ str(x2)+ "] is "+ str(Fraction(area)) + " or " + str(area))
        
        
    ##Graphing the function
    elif insertCal == "3":

        #Asking for a domain
        print("__________________________________________________________________________________________________")
        domain = input("Enter the interval to be graphed: (seperated by a space)")
        #Asking for what step to graph by
        step = float(input("Enter by what step is needed to be graphed:"))
        print("__________________________________________________________________________________________________")
        domainS = domain.split(" ")
        x1, x2 = float(domainS[0]), float(domainS[1])
        xV, xVal= x1, []

        #Graphing using pylab
        while xV <= x2+step:
            xVal.append(xV)
            xV+=step
            
        y,m,a = [],[],[]
        
        for i in xVal:
            y.append(f(i))
            m.append(deriv(i))
            a.append(integral(i))
            
        #Graphing f(x) 
        pylab.subplot(2,2,1)
        pylab.title("Given Function")
        pylab.xlabel('x')
        pylab.ylabel('y')
        pylab.plot(xVal, y, color='blue')
        pylab.grid()
        
        #Graphing f'(x) 
        pylab.subplot(2,2,2)
        pylab.title("Derivative Function")
        pylab.xlabel('x')
        pylab.ylabel('y')
        pylab.plot(xVal, m, color='green')
        pylab.grid()
        
        #Graphing F(x) 
        pylab.subplot(2,2,3)
        pylab.title("Integral Function")
        pylab.xlabel('x')
        pylab.ylabel('y')
        pylab.plot(xVal, a, color='red')
        pylab.grid()
     
      
        #Dimensions of the graphs
        pylab.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)
        
    else:
        print("\nInvalid input, Enter a valid input")
        continue
    
    
    #Asking if the user is finished:
    done = input("\nIf you are finished with the program press \"Enter\" if not any other key:")
    
pylab.show()
