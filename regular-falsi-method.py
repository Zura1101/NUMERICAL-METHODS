import sympy as sym
from sympy import *
x=symbols('x')
a=2
b=3
fx=x**3-2*x-5
for i in range(20):

    fa=fx.subs(x,a)
    fb=fx.subs(x,b)



    afb=a*fb
    bfa=b*fa
    xi=float((afb-bfa)/(fb-fa))
    fxi = fx.subs(x, xi)
    print("a\t=",a,"\t\t\t\t\tf(a)\t=",fa,"\t\t\t\tb\t=",b,"\t\t\t\t\tf(b)\t=",fb,"\t\t\t\txi\t=",xi,'\t\t\t\t\tf(xi)\t=',fxi)

    if fa<0 and fxi<0:
        a=xi
    else:
        b=xi
