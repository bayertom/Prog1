import math
from math import *
import sys

#y = sim(0)

#Raising exception
def radius(p):
    if p >=0:
        return p / (2 * pi)
    else:
        raise ValueError('Perimeter < 0', p)

#Preconditions and error codes
def f1(x):
    if len(x) < 2:
        return -1
    if x[1] == 0:
        return -2
    if x[0]>0 and x[1]<0 or x[0]<0 and x[1]>0:
        return -3
    return (x[0]/x[1])**0.5

#Exceptions and error codes
def f2(x):
    try:
        return (x[0]/x[1])**0.5
    except IndexError:
        return -1
    except ZeroDivisionError:
        return -2
    except ValueError:
        return -3

#Preconditions and exceptions
def f3(x):
    if len(x) < 2:
        raise IndexError('Bad index', x)
    if x[1] == 0:
        raise ZeroDivisionError('Divide by zero', x)
    if x[0]>0 and x[1]<0 or x[0]<0 and x[1]>0:
        raise ValueError('Result is negative', x)
    return (x[0]/x[1])**0.5

#Exceptions
def f4(x):
    try:
        return (x[0]/x[1])**0.5
    except IndexError as e:
        raise e
    except ZeroDivisionError as e:
        raise e
    except ValueError as e:
        raise e

#Raising exceptions
r = radius(-10)
print(r)

#Preconditions
x = [1, 1]
x = [1, -1]
x = [1, 0]
y = f(x)

#Exceptions and error codes
y = f2(x)

#Preconditions and exceptions
try:
    y = f3(x)
except IndexError as e:
    print(e)
except ArithmeticError as e:
    print(e)
print(y)

#Exceptionsdes
y = f4(x)