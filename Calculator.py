#Anton Kanugalwattage
#May 4, 2019
#Calculator for ploynomials to calculate roots, slope, area under curve and graphing.
import pylab

###Getting the function from user
checkFunc = 0
while checkFunc !="1":   
    
    #Scanning
    maxPower = input("Enter the exponents in the function separated by a space:")
    coeff = input("Enter the coefficients from the order of exponents separated by a space:")
        
    #Getting powers and coefficients out of the given input
    powerList = maxPower.split(" ")
    coeffList = coeff.split(" ")
    
    #Checking if the function is correct
    if len(coeffList)!=len(powerList):
        print("More coefficients or exponents than the other, enter your function appropriately again")
        continue 
            
    #Printing the function in a readable sense for the user
    print("-------------------------------------------------------------------------")
    z=0
    for i in range(len(coeffList)):
        if z < len(coeffList)-1:
            print(str(coeffList[i])+"x^"+str(powerList[i]) ,end=" + ")
        z+=1
    #Printing the last part of the polynomial to avoid "+" at the end
    if len(coeffList)-z+1==0:
        print(coeffList[-1])
    else:
        print(str(coeffList[-1])+ "x^" + str(powerList[-1]))
    checkFunc = input("\nIf this is the correct function enter \"1\" if not enter any other key:")

    
###Calculating values from the given function
def f(x):
    yVal =0
    for i in range(len(coeffList)):
        yVal += float(coeffList[i])*(x**(float(powerList[i])))       
    return yVal



###while loop till the user is finished with the operations
done = "0"
while done != "1":
    
    #Asking user for what calculator is to be used
    print("-------------------------------------------------------------------------")
    print("For Derivative Calculator enter \"2\":\nFor Definite Integral enter \"3\":")
    print("For a graph of the function enter \"4\": (Warning the program must be terminated for graphing to execute)")
    print("To end the program enter \"0\":")

    insertCal = input("")
    if insertCal == "0":
        break
        
        
    ##Derivative Calculator
    elif insertCal == "2":
        print("-------------------------------------------------------------------------")
        x = float(input("Enter the x value:"))    
        m = (f(x+1e-8)-f(x))/1e-8
        print("-------------------------------------------------------------------------")
        print("\nThe slope at the point (" + str(x) + "," +str(f(x)) +") is approximately " + str(round(m,4)))
    
    
    ##Definite Integral
    elif insertCal == "3":
        
        #Asking user for interval and num of slices
        print("-------------------------------------------------------------------------")
        intervalInput = input("Enter an interval that f(x) is continuous to find the area: (seperated by a space)")
        intervalInt = intervalInput.split(" ")
        x1, x2 = float(intervalInt[0]), float(intervalInt[1])
        step = float(input("Enter number of slices to calculate area: (higher number slices = higher accuracy)"))
        
        #Calculation area using Riemann Summation
        dx=(x2-x1)/step
        xm,area=x1,0
        while xm<=x2:
            area += f(xm) * dx
            xm += dx
        print("-------------------------------------------------------------------------")
        print(round(area,4))
        
        
    ##Graphing the function
    elif insertCal == "4":

        #Asking for a domain
        print("-------------------------------------------------------------------------")
        domain = input("Enter the interval to be graphed: (seperated by a space)")
        #Asking for what step to graph by
        step = float(input("Enter by what step is needed to be graphed:"))
        domainS = domain.split(" ")
        x1, x2 = float(domainS[0]), float(domainS[1])
        xV, xVal= x1, []

        #Graphing using pylab
        while xV <= x2:
            xVal.append(xV)
            xV+=step
        y = []
        
        for i in xVal:
            y.append(f(i))
        print("-------------------------------------------------------------------------")
        pylab.title("Graph of the given function")
        pylab.plot(xVal,y)
        pylab.show
        
        
    else:
        print("\nInvalid input, Enter a valid input")
        continue
    
    
    #Asking if the user is finished:
    done = input("\nIf you are finished with the program enter \"1\" if not enter any other key:")
