'''
Anton Kanugalwattage
May 4, 2019
Calculator for ploynomials, Overview:
- Derivative, Slope at a point
- Integral, Definite Integral
- Graphing
'''

import matplotlib
matplotlib.use("TKAgg")
print(matplotlib.get_backend())
from matplotlib import pyplot as pylab
import tkinter as tk
from math import *
from fractions import Fraction

H, W = 500, 600

def calculator(func):
	try:	
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

			elif len(x[i])==2 and i%2==0 and x[i][0]=="":
				coeffList.append(x[i-1][0]+"1")
				powerList.append(x[i][1][1:])
		
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


		##Printing the Derivative function
		#Removing the 0 coeff case
		derivCoeffUP,derivExpListUP=[], []
		for i in range(len(derivCoeff)):
			if derivCoeff[i]!=0:
				derivCoeffUP.append(derivCoeff[i])
				derivExpListUP.append(derivExpList[i])
		
		z=0
		deriv = ""
		for i in range(len(derivCoeffUP)):
			if z < len(derivCoeffUP)-1:
				if derivExpListUP[i]==1.0:
					deriv += str(round(derivCoeffUP[i],3))+"x + " 
				elif derivExpListUP[i]==0 and derivCoeffUP[i] !=0 and derivExpListUP[i]!=-1:
					deriv += str(round(derivCoeffUP[i],3)) + " + "
				elif derivCoeffUP[i] !=0 and derivExpList[i] !=-1:
					deriv += str(round(derivCoeffUP[i],3))+"x^"+str(derivExpListUP[i]) + " + "
			z+=1

		#Printing the last part of the derivative to avoid "+" at the end
		if derivExpListUP[-1]==0 and derivCoeffUP[-1] !=0:
			deriv += str((round(derivCoeffUP[-1],3)))
		elif derivExpListUP[-1]==1.0:
			deriv += (str(round(derivCoeffUP[i],3))+"x")
		elif derivCoeffUP[-1] !=0:
			deriv += (str(round(derivCoeffUP[-1],3))+ "x^" + str(derivExpListUP[-1]))


		##Printing the Integral function
		integ,z='',0
		print("Integral is; F(x) = ", end = "")
		for i in range(len(intCoeff)):
			if intExpList[i]==1.0:
				integ+=(str(round(intCoeff[i],3))+"x" + " + ")
			elif intCoeff[i]!=0.0 and intExpList[i]!=0.0:
				integ+=(str(round(intCoeff[i],3))+"x^"+str(intExpList[i]) + " + ")
			elif intExpList[i]==0.0:
				integ+=(str(round(intCoeff[i],3))+ "ln|x|" + " + ")
		integ+=("C")


		###Calculating values from the given function
		def f(x):
			y =0
			for i in range(len(coeffList)):
				y += float(coeffList[i])*(x**(float(powerList[i])))       
			return y


		###Calculating values from the derivative function
		def derivative(x):
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

		x1 ,x2 = 0.1 ,15.0
		step=0.1
		xV, xVal= x1, []
		while xV <= x2+step:
			xVal.append(xV)
			xV+=step
		y,m,a=[],[],[]

		for i in xVal:
			y.append(f(i))
			m.append(derivative(i))
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
		
	except:
		deriv,integ = "Invalid Expression","Invalid Expression"
        
        
    #Dimensions of the graphs
	pylab.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)

	labelDeriv['text'] = deriv
	labelInteg['text'] = integ
	pylab.show()    

#TKinter GUI
root = tk.Tk()
root.title("MathOps Calculator by Anton K (2019)")
canvas = tk.Canvas(root, height=H, width=W)
canvas.pack()

backImg = tk.PhotoImage(file='./mathops.png')
backLbl = tk.Label(root, image=backImg)
backLbl.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#9b9da0', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=70)
entry.place(relwidth=0.68, relheight=1)
entry.bind("<Return>", (lambda event: calculator(entry.get())))

button = tk.Button(frame, text="Calculate", font=(40), cursor="hand2",command=lambda: calculator(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

frameDeriv = tk.Frame(root, bg='#9b9da0', bd=10)
frameDeriv.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.3, anchor='n')

frameInteg = tk.Frame(root, bg='#9b9da0', bd=10)
frameInteg.place(relx=0.5, rely=0.575, relwidth=0.75, relheight=0.3, anchor='n')

labelDeriv = tk.Label(frameDeriv)
labelDeriv.place(relwidth=1, relheight=1)

labelInteg = tk.Label(frameInteg)
labelInteg.place(relwidth=1, relheight=1)

root.mainloop()
