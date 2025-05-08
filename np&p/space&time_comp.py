import sys
import numpy as np
import time

# Memory comparison
py_list = list(range(1000))
np_array = np.array(py_list)

print("Python list size:", sys.getsizeof(py_list))         # ~9000+ bytes
print("NumPy array size:", np_array.nbytes)               # ~4000 bytes

# Speed comparison
start = time.time()
sum([x**2 for x in py_list])
print("List time:", time.time() - start)

start = time.time()
np_array**2
print("NumPy time:", time.time() - start)
