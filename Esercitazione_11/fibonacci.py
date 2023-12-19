"""
Filename: fibonacci.py
Demonstrates the use of ctypes with three functions:

    (1) fib(a)
    (2) fibseries(b)
    (3) fibmatrix(c)
"""

import numpy as nm
import ctypes as ct

# Load the library as _libfibonacci.
# Why the underscore (_) in front of _libfibonacci below?
# To mimimise namespace pollution -- see PEP 8 (www.python.org).
# _libfibonacci = nm.ctypeslib.load_library('libfibonacci', '.')

_libfibonacci = ct.cdll['/Users/enricoduca/Documents/Università/MCF/Rep/Esercitazione_11/libfibonacci.so']

_libfibonacci.fib.argtypes = [ct.c_int] #  Declare arg type, same below.
_libfibonacci.fib.restype  =  ct.c_double  #  Declare result type, same below.


def fib(a):
    return _libfibonacci.fib(int(a))
