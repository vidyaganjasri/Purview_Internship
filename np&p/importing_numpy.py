''' 1. Using Full Module
    numpy.array() converts the list [1, 2, 3] into a NumPy array.
    Accessed via the full module name.'''
import numpy
numpy.array([1, 2, 3])


'''2.Using Alias (np)
  Same function as above, but using the alias np.
  This is the most popular method used in practice.'''
import numpy as np
np.array([1, 2, 3])


'''3.Importing Only the array Function
    You import just the array function.
    You can use it directly without a prefix.'''
from numpy import array
array([1, 2, 3])


