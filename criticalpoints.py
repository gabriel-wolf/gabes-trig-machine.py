from __future__ import division


# from flask import Flask
# import sys

# from flask import Flask, render_template, request, redirect, Response
# import random, json
# from http.server import HTTPServer, BaseHTTPRequestHandler, test
# import ssl
# from http.server import SimpleHTTPRequestHandler
import webbrowser

from sympy import *
from sympy import sin, cos, tan, asin, atan, acos, Function, diff
from sympy import limit
from sympy.solvers import solve
from sympy import ImageSet, Lambda, pi, S, Dummy, pprint
from sympy import Point
from sympy.printing.latex import print_latex
from sympy.printing.dot import dotprint
import re

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
x, y, z, a = symbols('x y z a')
n = Dummy('n')
init_printing(use_latex='mathjax')

import argparse

# sin((11*pi*x)/(6))
# tan((-2*pi*x)/(3))

ap = argparse.ArgumentParser()
ap.add_argument("-e", "--equation", required=False, default="sin((11*pi*x)/(6))",
	help="equation")
ap.add_argument("-a", "--angle", required=False, default="pi/6",
	help="angle")
args = vars(ap.parse_args())




# file = open("renderpage.html","r") 
# # print(file.read())
# filecontentsfull = file.read()

# exprarray = [sin(2*x)]


# result = re.search('<div hidden=True id="main">(.*)</div>', filecontentsfull)
# print(result.group(1))
# if (str(result.group(1)) == ""):
#     print("use default expr")
# else:
#     print("use custom expr")
#     exprarray[0] = result.group(1)

# print(exprarray[0])


# <div hidden=True id="main">fdf</div>


f = Function('f')
# expr = sin(2*x)
from sympy.parsing.sympy_parser import parse_expr

# expr = parse_expr(exprarray[0])
expr = parse_expr(args["equation"])
# exprstr = 'np.sin(x)'


uinput = input("Enter Equation: ")
if (uinput == ""):
    None
else:
    expr = parse_expr(uinput)



exprangle = args["angle"]


sol = solve((diff(expr, x)), x)

# print("Invertable domain: ")
# print(pretty(solve((diff(expr, x)), x)))
# print("Every Domain Line: ")
# print(pretty(sstr(solve((diff(expr, x)), x)[0]) + " + " + sstr(sstr(expr.period()) + "*n and " + sstr(solve((diff(expr, x)), x)[1])) + " + " + sstr(expr.period()) + "*n"))


limxone = int((pi/4)+(pi*-1))
limxtwo = int(((3*pi)/4) + (pi*1))
 
from sympy import latex, Rational
from sympy.abc import tau
from sympy import latex, simplify
from sympy.abc import x, y, mu, r, tau
import codecs
n = Dummy('n')



def inversesolve(func):
    newxexpr = func.replace("x","y")
    # print(newxexpr)
    inverseexpr = (Eq(x,newxexpr))
    # print(inverseexpr)
    # print(solve(inverseexpr,y))
    return solve(inverseexpr,y)


def simplifyme(expr):
    simplifyexpr = simplify(expr)
    # print(simplifyexpr)
    return(simplifyexpr)








# print(inversesolve(expr))
# print(latex(expr, mode='inline'))
# print(latex(((solve((diff(expr, x)), x)[0]) + ((expr.period())*n)), mode='inline'))
# print(latex(((solve((diff(expr, x)), x)[1]) + ((expr.period())*n)), mode='inline'))


# latex(expr.period(), mode='inline')
# latex(expr, mode='inline')
###### latex(((solve((diff(expr, x)), x)[0]) + ((expr.period())*n)), mode='inline')
######## latex(((solve((diff(expr, x)), x)[1]) + ((expr.period())*n)), mode='inline')



# print(expr)

# assert periodicity(tan(x), x, check=True) == pi
# assert periodicity(sin(x) + cos(x), x, check=True) == 2*pi
# print(lambda: periodicity(sec(x), x, check=True))
# print(lambda: periodicity(sin(x*y), x, check=True))

# print(periodicity(tan(x), x))
# print(periodicity(sin(x) + cos(x), x))

# print(periodicity(expr, x))
# print(periodicity(sin(exprangle) + cos(exprangle), x))





file = open("readmehere.txt","w") 

file.write(latex(expr, mode='inline'))
file.write("\n")
try:
    file.write(latex(((solve((diff(expr, x)), x)[0]) + ((expr.period())*n)), mode='inline'))
    pass
except:
    file.write("None")
    pass
file.write("\n")
try:
    file.write(latex(((solve((diff(expr, x)), x)[1]) + ((expr.period())*n)), mode='inline'))
    pass
except:
    file.write("None")
    pass
file.write("\n")
file.write(latex(solve(diff(expr, x),x), mode='inline'))
file.write("\n")
try:
    file.write(latex((expr).period(), mode='inline'))
    pass
except:
    file.write(latex(periodicity(expr, x), mode='inline'))
    pass
file.write("\n")
from sympy import Rel
p = Point(cos(exprangle), sin(exprangle))
if ((cos(exprangle)) > 0) and ((sin(exprangle)) > 0):
    # print("quad 1")
    file.write("1")
elif ((cos(exprangle)) < 0) and ((sin(exprangle)) > 0):
    # print("quad 2")   
    file.write("2")
elif ((cos(exprangle)) < 0) and ((sin(exprangle)) < 0):
    # print("quad 3")
    file.write("3")
elif ((cos(exprangle)) > 0) and ((sin(exprangle)) < 0):
    # print("quad 4")
    file.write("4")
else:
    file.write("None")
file.write("\n")
file.write(latex(inversesolve(expr), mode='inline'))
file.write("\n")
file.write(latex(simplifyme(expr), mode='inline'))




file.close() 


# webbrowser.open("renderpage.html")




























#
#pprint(diff(expr, x,0))
#pprint(diff(expr, x,1))
#pprint(diff(expr, x,2))
#
#pprint(limit((diff(expr, x)), x, 0, '-'))
#pprint(limit((diff(expr, x)), x, 0, '+'))
#pprint(solve([sin(x + y), cos(x - y)], [x, y]))
#pprint(limit(expr, y, 0, '-'))
#pprint(limit(expr, y, oo))
#pprint(ImageSet(Lambda(n, 2*pi*n), S.Integers), use_unicode=False)
#pprint(integrate(expr, x))





