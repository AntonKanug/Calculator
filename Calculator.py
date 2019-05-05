#Anton Kanugalwattage
#May 4, 2019
#Calculator for ploynomials to calculate roots, slope, area under curve and graphing.
import pylab

###Getting the function from user
insert = 0
while insert !="1":   
    
    #Scanning
    maxPower = int(input("Enter the highest power in the funciton:"))
    coeff = input("Enter the coeffiecents from descending order of power sperated by a space:")
        
    #Getting coefficents out of the given input
    coeffList = coeff.split(" ")
    
    #Checking if the function is correct
    if len(coeffList)>maxPower+1:
        print("More coefficents than powers enter your funtion appropriately again")
        continue 
            
    #Printing the function in a readable sense for the user
    print("-------------------------------------------------------------------------")
    z=0
    for i in coeffList:
        if z < len(coeffList)-1:
            print(str(i)+"x^"+str(maxPower-z) ,end=" + ")
        z+=1
    #Printing the last part of the polynomial to avoid "+" at the end
    if maxPower-z+1==0:
        print(coeffList[-1])
    else:
        print(str(coeffList[-1])+ "x^" + str(maxPower-z+1))
    insert = input("\nIf this is the correct function enter \"1\" if not enter any other key:")

    
###Calcuating values from the given function
def f(x):
    yVal, power, z=0, maxPower, 0
    for i in coeffList:
        yVal += float(i)*(x**(power-z))
        z+=1        
    return yVal



###while loop till the user is finished
done = "0"
while done != "1":
    
    #Asking user for what calculator is to be used
    print("-------------------------------------------------------------------------")
    print("For Deravitive Calculator enter \"2\":\nFor Definite Integral enter \"3\":")
    print("For a graph of the function enter \"4\": (Warning the program must be terminateed for graphing to execute)")
    print("To end the program enter \"0\":")

    insertCal = input("")
    if insertCal == "0":
        break
        
        
    ##Deravitve Calculator
    elif insertCal == "2":
        print("-------------------------------------------------------------------------")
        x = float(input("Enter the x value:"))    
        m = (f(x+1e-8)-f(x))/1e-8
        print("-------------------------------------------------------------------------")
        print("\nThe slope at the point (" + str(x) + "," +str(f(x)) +") is approxrimately " + str(round(m,4)))
    
    
    ##Definite Integral
    elif insertCal == "3":
        
        #Asking user for interval and num of slices
        print("-------------------------------------------------------------------------")
        intervalInput = input("Enter the interval to find the area: (seperated by a space)")
        intervalInt = intervalInput.split(" ")
        x1, x2 = float(intervalInt[0]), float(intervalInt[1])
        step = float(input("Enter number of slices to calculate area: (higher number slices = higher accuray)"))
        
        #Calculation area using Riemann Summation
        dx=(x2-x1)/step
        xm,area=x1,0
        while xm<=x2:
            area += f(xm) * dx
            xm += dx
        print("-------------------------------------------------------------------------")
        print(round(area,4))
        
        
    ##Graphing
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
