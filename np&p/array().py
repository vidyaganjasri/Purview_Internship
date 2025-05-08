'''The array() function is used to create a NumPy array from a list, tuple, or other array-like objects.
  Purpose of NumPy array:
  Faster and more memory-efficient than Python lists'''
import numpy as np
arr = np.array([1, 2, 3])
print(arr)       # Output: [1 2 3]
print(arr + 5)   # Output: [6 7 8] → Vectorized operation
'''In traditional Python lists, if you want to change every element (like add, multiply, etc.), you must use a loop or list comprehension.
But in NumPy arrays, these changes can be done directly in one line using vectorized operations'''
