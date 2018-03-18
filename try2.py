
from matplotlib import pylab
from pylab import plot,show
from numpy import array,linspace,sqrt,sin
from numpy.linalg import norm

import math
trig={
    'sin(x)':'sin(x)',
    'cos(x)':'(1/sin(x))',
    'tan(x)':'sin(x)/(1/sin(x))',
}
def fixedp(f,x0,tol=10e-5,maxiter=100):
 """ Fixed point algorithm """
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




finput=input("What do you wanna do with x? ")
if(finput=="cos(x)" or finput=="tan(x)"):
    finput=trig[finput]
f = lambda x : eval(finput)


x_start = .5
xf,xp = fixedp(f,x_start)

x = linspace(0,2,100)
y = f(x)
plot(x,y,xp,f(xp),'bo',
     x_start,f(x_start),'ro',xf,f(xf),'go',x,x,'k')

print("Root is converging to " ,xf)
show()