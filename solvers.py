from __future__ import division
import math
from math import *
from sympy import *
from sympy import sin, cos, tan, asin, atan, acos
from sympy import Function, diff, limit, ImageSet, Lambda, pi, S, Dummy, pprint, Point
from sympy import expand, factor
from sympy.solvers import solve
from sympy.printing.latex import print_latex
from sympy.printing.dot import dotprint
import re
import argparse
from sympy.parsing.sympy_parser import parse_expr
from sympy import latex, Rational
from sympy.abc import tau
from sympy import latex, simplify
from sympy.abc import x, y, mu, r, tau
import codecs

x, y, z, t = symbols('x y z t')
k, m, n = symbols('k m n', integer=True)
f, g, h = symbols('f g h', cls=Function)
x, y, z, a = symbols('x y z a')
n = Dummy('n')
f = Function('f')
init_printing()


def q_starting(expr, str):
    return expr.startswith(str)

def q_betweenstr(expr,start):
    try:
        result = (re.search('%s(.*)%s' % ((start + '('), ')'), expr).group(1))[1:-1]
        return(result)
    except AttributeError:
        return('FAIL')


def util_breakatcomma(expr):
    print("not ready yet")
    return("no")

def f_evaluatef(expr):
    return (S(expr).evalf())

def f_expand(expr):
    return expand(expr)

def f_factor(expr):
    return factor(expr)

def f_solve(expr, variables):
    return (solve(S(expr), S(variables)))

def f_roots(expr, variables):
    return (roots(S(expr), S(variables)))

def f_nsimplify(expr):
    nsimplify(e)


while true:
    uinput = input("\n>> ")
    if (q_starting(uinput, 'expand') == True):
        func = q_betweenstr(uinput, 'expand')
        print(f_expand(func))
    elif (q_starting(uinput, 'factor') == True):
        func = q_betweenstr(uinput, 'factor')
        print(f_factor(func))
    elif (q_starting(uinput, 'solve') == True):
        func = q_betweenstr(uinput, 'solve')
        funcarray = func.split(',',1)
        print(f_solve(funcarray[0], S(funcarray[1])))
    elif (q_starting(uinput, 'roots') == True):
        func = q_betweenstr(uinput, 'roots')
        funcarray = func.split(',',1)
        print(f_roots(S(funcarray[0]), S(funcarray[1])))
    elif(uinput.lower() == "quit"):
        exit(0)
    else:
        print(str(f_evaluatef(uinput)))
    

