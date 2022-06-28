"""
Plot the logistic function


Implement a logistic function with two features ``(x1, x2)``. Set the
two coefficients to ``0.5`` and ``3.0``, respectively. Write a small
program that tries a range of values for ``(x1, x2)``.

Examine, how ``p`` changes.

*code from https://github.com/krother/python_machine_learning, MIT License*
"""
from pylab import *

def logistic(x):
    return 1.0 / (1 + math.exp(-x))

x = [xx / 10.0 for xx in range(-100, 100)]
y = [logistic(xx) for xx in x]

figure()
plot(x,y)
title('logistic function')
savefig('logistic_function.png')
