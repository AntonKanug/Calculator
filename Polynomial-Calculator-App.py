'''
Anton Kanugalwattage
May 18, 2019
Calculator for polynomials, Overview:
- Derivatives, Slope at a point
- Integrals, Definite Integral
- Graphing
Demo: https://youtu.be/qyUpNjB71sk
'''


import matplotlib
matplotlib.use("TKAgg")
from matplotlib import pyplot as pylab
import tkinter as tk
from math import *
from fractions import Fraction



H, W = 494, 594
root = tk.Tk()
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
					if derivCoeffUP[i]==1:
						deriv+="x^"+str(round(derivExpListUP[i],3)) + " + "
					elif derivExpListUP[i]==1.0:
						deriv += str(round(derivCoeffUP[i],3))+"x + " 
					elif derivExpListUP[i]==0 and derivCoeffUP[i] !=0 and derivExpListUP[i]!=-1:
						deriv += str(round(derivCoeffUP[i],3)) + " + "
					elif derivCoeffUP[i] !=0 and derivExpList[i] !=-1:
						deriv += str(round(derivCoeffUP[i],3))+"x^"+str(round(derivExpListUP[i],3)) + " + "
				z+=1

			#Printing the last part of the derivative to avoid "+" at the end
			if derivCoeffUP[-1] ==0:
				deriv += "0"
			elif derivCoeffUP[-1]==1:
				deriv+="x^"+str(round(derivExpListUP[-1],3))
			elif derivExpListUP[-1]==0 and derivCoeffUP[-1] !=0:
				deriv += str((round(derivCoeffUP[-1],3)))
			elif derivExpListUP[-1]==1.0:
				deriv += (str(round(derivCoeffUP[i],3))+"x")
			elif derivCoeffUP[-1] !=0:
				deriv += str(round(derivCoeffUP[-1],3))+ "x^" + str(round(derivExpListUP[-1],3))


		##Printing the Integral function
		integ,z='F(x) = ',0

		for i in range(len(intCoeff)):
			if intCoeff[i]==1 and intExpList[i]!=0:
				integ+="x^"+str(round(intExpList[i],3)) + " + "
			elif intExpList[i]==1.0:
				integ+=str(round(intCoeff[i],3))+"x" + " + "
			elif intCoeff[i]!=0.0 and intExpList[i]!=0.0:
				integ+=str(round(intCoeff[i],3))+"x^"+str(round(intExpList[i],3)) + " + "
			elif intExpList[i]==0.0:
				integ+=str(round(intCoeff[i],3))+ "ln|x|" + " + "
		integ+="C"


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

		###Graphing	
		if x1!="" and x2!="":
			x1,x2 = float(x1),float(x2)
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

			#Title of the tab
			pylab.figure(num='Graphs - MathOps Calculator (2019)')

			#Graphing f(x) 
			pylab.subplot(2,2,1)
			pylab.title("Given Function, f(x)")
			pylab.xlabel('x')
			pylab.ylabel('y') 
			pylab.plot(xVal, y, color='blue')
			pylab.grid()
				
				
			#Graphing f'(x) 
			pylab.subplot(2,2,2)
			pylab.title("Derivative Function, f'(x)")
			pylab.xlabel('x')
			pylab.ylabel('y')
			pylab.plot(xVal, m, color='green')
			pylab.grid()
				
				
			#Graphing F(x) 
			pylab.subplot(2,2,3)
			pylab.title("Integral Function, F(x)")
			pylab.xlabel('x')
			pylab.ylabel('y')
			pylab.plot(xVal, a, color='red')
			pylab.grid()
			
			#Dimensions of the graphs
			pylab.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.5, wspace=0.35)

	#Invalid Expressions
	except:
		deriv,integ = "Invalid Expression","Invalid Expression"
        

	#Outputting Derivative and Integral
	labelDeriv['text'] = deriv
	labelInteg['text'] = integ

	#Showing the graphs in a new window
	if x1!="" and x2!="":
		pylab.show()	

###TKinter GUI

root.title("MathOps Calculator (2019)")
canvas = tk.Canvas(root, height=H, width=W,bg="black",bd=0)
canvas.pack()

icon = tk.PhotoImage(file='icon.gif')
root.tk.call('wm', 'iconphoto', root._w, icon)

#Background
backImg = tk.PhotoImage(file='mathops.png')
backLbl = tk.Label(root, image=backImg)
backLbl.place(relwidth=1, relheight=1)


###Creating frames
def createFrame  (x,y,w,h,border,anc):
	frame  = tk.Frame(root, bg='#CDCDCD', bd=border)
	frame.place(relx=x, rely=y, relwidth=w, relheight=h,anchor=anc)
	return frame


###Creating Labels
def createLabel (frame,font,x,y,text,bg):
	text = tk.Label(frame, font=font, text = text, bg=bg)
	text.place(relx=x, rely=y)


###Creating Entries
def createEntry (frame,font,x,y,w,h):
	entry = tk.Entry(frame,font=font)
	entry.place(relx=x, rely=y, relwidth=w, relheight=h)
	return entry

#Frames
topFrame = createFrame(0.5,0.08,0.75,0.1,5,"n")
calcFrame = createFrame(0.5,0.21,0.3,0.075,2,"n")


#Entry for function
func = createEntry(topFrame, 70, 0.1, 0, 0.572, 1)


#Text for f(x)
createLabel(topFrame,60,0,0.21,"f(x) =",'#CDCDCD')


#Text for interval
createLabel(topFrame,60,0.68,0.21,"on [",'#CDCDCD')
createLabel(topFrame,60,0.85,0.21,",",'#CDCDCD')
createLabel(topFrame,60,0.98,0.21,"]",'#CDCDCD')


#Interval (x1,x2)
x1 = createEntry(topFrame, 70, 0.76, 0.16, 0.08, 0.75)
x2 = createEntry(topFrame, 70, 0.89, 0.16, 0.08, 0.75)


#Binding Enter Key
if x1.get()=="" and x2.get()=="":
	func.bind("<Return>", (lambda event: calculator(func.get(),"","")))
else:
	func.bind("<Return>", (lambda event: calculator(func.get(),float(x1.get()),float(x2.get()))))
x2.bind("<Return>", (lambda event: calculator(func.get(),float(x1.get()),float(x2.get()))))

#Calculate Button
button = tk.Button(calcFrame, text="Calculate", font=(40), cursor="hand2",command=lambda: calculator(func.get(),x1.get(),x2.get()))
button.place(relheight=1, relwidth=1)

##Outputting the results
frameDeriv = createFrame(0.5,0.35,0.75,0.25,0.3,"n")
frameInteg = createFrame(0.5,0.65,0.75,0.25,0.3,"n")

#White Background
labelDeriv = tk.Label(frameDeriv)
labelDeriv.place(relwidth=1, relheight=1)

labelInteg = tk.Label(frameInteg)
labelInteg.place(relwidth=1, relheight=1)

createLabel(frameDeriv, 60,0.37,0.2,"Derivative Function:","#FFFFFF")
createLabel(frameInteg, 60,0.37,0.2,"Integral Function:","#FFFFFF")

#Main Loop 
root.mainloop()

