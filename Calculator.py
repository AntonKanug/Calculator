#Anton Kanugalwattage, 2019
#Calculator

###Getting the function
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
    z=0
    for i in coeffList:
        print(str(i)+"x^"+str(maxPower-z) ,end=" ")
        z+=1
    insert = input("\n If this is the correct function enter \"1\" if not enter any other key:")

    
###Calcuating values from the given function
def f(x):
    yVal, power, z=0, maxPower, 0
    for i in coeffList:
        yVal += int(i)*(x**(power-z))
        z+=1        
    return yVal



###while loop till the user is finished
done = "0"
while done != "1":
    
    #Asking user for what calculator is to be used
    insertCal = input(" For Deravitive Calculator enter \"2\":\n For Definite Integral enter \"3\":\n For a graph of the function enter \"4\" (Warning the program wil terminate after graphing is executed):")

    ##Deravitve Calculator
    if insertCal == "2":
        x = int(input("Enter the x value:"))    
        m = (f(x+1e-8)-f(x))/1e-8
        print(round(m,4))
     
    
    
    ##Definite Integral
    
    
    
    ##Graphing
    if insertCal == "4":
        import pylab

        #Asking for a domain
        domain = input("Enter the domain to be graphed: (seperated by a space)")
        #Asking for what step to graph by
        step = float(input("Enter by what step is needed to be graphed:"))
        domainS = domain.split(" ")
        x1, x2 = int(domainS[0]), int(domainS[1])
        xV, xVal= x1, []

        #Graphing using pylab
        while xV <= x2:
            xVal.append(xV)
            xV+=step
        y = []
        
        for i in xVal:
            y.append(f(i))
        pylab.title("Graph of the given function")
        pylab.plot(xVal,y)
        pylab.show
        #The loop need to be ended inorder for the graph to appear
        break
    
    
    #Asking if the user is finished:
    done = input("\nIf you are finished with the program enter \"1\" if not enter any other key:")
