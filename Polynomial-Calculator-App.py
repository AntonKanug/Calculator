'''
Anton Kanugalwattage
May 18, 2019
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

H, W = 494, 594

def calculator(func,x1,x2):
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

			elif len(x[i])==2 and i%2==0 and x[i][1]=="" and x[i][0]=="":
				coeffList.append(x[i-1][0]+"1")
				powerList.append(1)

			elif len(x[i])==2 and i%2==0 and x[i][0]=="":
				coeffList.append(x[i-1][0]+"1")
				powerList.append(x[i][1][1:])

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
		if len(derivCoeffUP)==0 and len(derivExpListUP)==0:
			deriv = "0"
		else:
			z=0
			deriv = "f'(x) = "
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
			if derivCoeffUP[-1] ==0:
				deriv += "0"
			elif derivExpListUP[-1]==0 and derivCoeffUP[-1] !=0:
				deriv += str((round(derivCoeffUP[-1],3)))
			elif derivExpListUP[-1]==1.0:
				deriv += (str(round(derivCoeffUP[i],3))+"x")
			elif derivCoeffUP[-1] !=0:
				deriv += (str(round(derivCoeffUP[-1],3))+ "x^" + str(derivExpListUP[-1]))


		##Printing the Integral function
		integ,z='F(x) = ',0
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
		if x1!=0 and x2!=0:
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

	#Outputting Derivative and Integral
	labelDeriv['text'] = deriv
	labelInteg['text'] = integ

	#Showing the graphs in a new window
	if x1!= 0 and x2!=0:
		pylab.show()	

#TKinter GUI
root = tk.Tk()
root.title("MathOps Calculator (2019)")
canvas = tk.Canvas(root, height=H, width=W,bg="black",bd=0)
canvas.pack()

icon = tk.PhotoImage(file='icon.gif')
root.tk.call('wm', 'iconphoto', root._w, icon)

#Background
backImg = tk.PhotoImage(file='mathops.png')
backLbl = tk.Label(root, image=backImg)
backLbl.place(relwidth=1, relheight=1)


#Top Frame
frame = tk.Frame(root, bg='#CDCDCD', bd=5)
frame.place(relx=0.5, rely=0.08, relwidth=0.75, relheight=0.1, anchor='n')

#Frame for Button
frame2 = tk.Frame(root, bg='#CDCDCD', bd=5)
frame2.place(relx=0.5, rely=0.20, relwidth=0.3, relheight=0.075, anchor='n')

#Entry for function
func = tk.Entry(frame, font=70)
func.place(relwidth=0.68, relheight=1)
func.bind("<Return>", (lambda event: calculator(func.get(),0,0)))

#Text for interval
text = tk.Label(frame,font=(60),text = "on [",bg='#CDCDCD')
text.place(relx=0.68,rely=0.21)

text2 = tk.Label(frame,font=(60),text = ",",bg='#CDCDCD')
text2.place(relx=0.85,rely=0.21)

text3 = tk.Label(frame,font=(60),text = "]",bg='#CDCDCD')
text3.place(relx=0.98,rely=0.21)

#Interval (x1,x2)
x1 = tk.Entry(frame, font=70)
x1.place(relx=0.76,rely =0.16,relwidth=0.08, relheight=0.75)

x2 = tk.Entry(frame, font=70)
x2.place(relx=0.89,rely =0.16,relwidth=0.08, relheight=0.75)
x2.bind("<Return>", (lambda event: calculator(func.get(),float(x1.get()),float(x2.get()))))

#Calculate Button
if x1.get()=="" and x2.get()=="":
    button = tk.Button(frame2, text="Calculate", font=(40), cursor="hand2",command=lambda: calculator(func.get(),0,0))
else:
	button = tk.Button(frame2, text="Calculate", font=(40), cursor="hand2",command=lambda: calculator(func.get(),float(x1.get()),float(x2.get())))
button.place(relheight=1, relwidth=1)

#Results
frameDeriv = tk.Frame(root, bg='#CDCDCD', bd=3)
frameDeriv.place(relx=0.5, rely=0.35, relwidth=0.75, relheight=0.25, anchor='n')

frameInteg = tk.Frame(root, bg='#CDCDCD', bd=3)
frameInteg.place(relx=0.5, rely=0.65, relwidth=0.75, relheight=0.25, anchor='n')

labelDeriv = tk.Label(frameDeriv)
labelDeriv.place(relwidth=1, relheight=1)

labelInteg = tk.Label(frameInteg)
labelInteg.place(relwidth=1, relheight=1)

derivT = tk.Label(frameDeriv,font=(60),text = "Derivative Function:")
derivT.place(relx=0.37,rely=0.2)

integT = tk.Label(frameInteg,font=(60),text = "Integral Function:")
integT.place(relx=0.37,rely=0.2)

#Main Loop 
root.mainloop()
