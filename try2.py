
from matplotlib import pylab
from pylab import plot,show
from numpy import *
from numpy.linalg import norm
trig={
    'csc(x)':'(1/sin(x))',
    'sec(x)':'(1/cos(x))'

}
def fixedp(f,x0,tol=10e-5,maxiter=100):
 e = 1
 itr = 0
 xp = []
 while(e > tol and itr < maxiter):
  x = f(x0)      # fixed point equation
  e = norm(x0-x) # error at the current step
  x0 = x
  xp.append(x0)  # save the solution of the current step
  itr = itr + 1
  print(itr,":",x)
 return x,xp

print("(x) is a collection of evenly spaced numbers ranging from 0-2")
finput=input("What do you wanna do with x? ")
start=input("Enter starting point: ")
if(finput=="csc(x)" or finput=="sec(x)"):
   finput=trig[finput]
f = lambda x : eval(finput)


x_start = float(start)
xf,xp = fixedp(f,x_start)

x = linspace(0,2,100)
y = f(x)
plot(x,y,xp,f(xp),'bo',
     x_start,f(x_start),'ro',xf,f(xf),'go',x,x,'k')

print("Root is converging to " ,xf)
show()