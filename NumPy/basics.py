# https://numpy.org/devdocs/user/quickstart.html
import numpy as np
a = np.arange(15).reshape(3, 5)
print(a)
print(a.shape)
print(a.ndim)
print(a.dtype.name) #'int32'
print(a.itemsize) #size in byte of each item
print(a.size)
print(type(a))

b = np.array([6, 7, 8], dtype=np.int16)
print(b)
print(type(b))
print(b.dtype.name)

b = np.array([(1.5,2,3), (4,5,6)])
print(b)
print(b.dtype.name) #'float64'

a = np.zeros((3, 4))
print(a)
a = np.ones( (2,3,4), dtype=np.int16 )
print(a)

# To create sequences of numbers, NumPy provides the arange function which is analogous to the Python built-in range, but returns an array.
a = np.arange( 10, 30, 5 )
print(a)

np.arange( 0, 2, 0.3 )
print(a) 
#But it's better to define the number of elements
from numpy import pi
a = np.linspace( 0, 2, 9 )  
print(a)
x = np.linspace( 0, 2*pi, 100 )
s = np.sin(x)
print(s)

b = np.arange(12).reshape(4,3)   
print(b)

c = np.arange(24).reshape(2,3,4)         # 3d array
print(c)

print(np.arange(10000))

print('\nbasic operations')
a = np.array( [20,30,40,50] )
b = np.arange( 4 )
c = a-b
print(c)
print(b**2)
print(10*np.sin(a))
print(a<35)

#elementwise product
A = np.array( [[1,1], [0,1]] )
B = np.array( [[2,0], [3,4]] )
print(A * B)
print(A @ B)
print(A.dot(B))

from numpy import random as ran
a = np.ones((2,3), dtype=int)
b = ran.random((2,3))
a *= 3
b += a
print(b)

#a += b cast error

# When operating with arrays of different types,
# the type of the resulting array corresponds to
# the more general or precise one (a behavior known as upcasting).
a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
c = a+b
print(c)
print(c.dtype.name)

# Many unary operations, such as computing the sum of all the elements in the array,
# are implemented as methods of the ndarray class.
a = ran.random((2,3))
print(a.sum())
print(a.min())
print(a.max())

#By default, these operations apply to the array as though it were a list of numbers,
# regardless of its shape. However,
# by specifying the axis parameter you can apply an operation along the specified axis of an array:
b = np.arange(12).reshape(3,4)
print(b.sum(axis=0)    )
print(b.min(axis=1))

# Universal Functions
B = np.arange(3)
print(np.exp(B))
print(np.sqrt(B))
C = np.array([2., -1., 4.])
print(np.add(B, C))

print('#Indexing, Slicing and Iterating')
a = np.arange(10)**3
print(a)
a[:6:2] = 1000
print(a)
b = a[ : :-1]                                 # reversed a
print(a)
print(b)

def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)
print(b[2,3])
print(b[0:5, 1]) # each row in the second column of b
print(b[ : ,1]) # equivalent to the previous example
print(b[0,:]) # printed as a row, even if a column
print(b[1:3, : ]) # each column in the second and third row of b
# When fewer indices are provided than the number of axes,
# the missing indices are considered complete slices:
print(b[-1])                                  # the last row. Equivalent to b[-1,:]

c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
                [[100,101,102],
                [110,112,113]]])
print(c.shape)
print(c[1,...])                                   # same as c[1,:,:] or c[1]
print(c[...,2])                                   # same as c[:,:,2]

# Iterating over multidimensional arrays is done with respect to the first axis:
for row in b:
    print(row)
for plan in c:
    print(plan)

for element in b.flat:
    print(element)
