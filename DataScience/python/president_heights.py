import numpy as np
import array

#L=list(range(10))
#A=array.array('i',L)
#A

#np.array([1,4,2,5,3])
#np.array([1,4,2,5,3],dtype='float32')
#np.array([range(i,i+3)for i in[2,4,6]])
####Creating arrays fom scratch
# np.zeros(10,dtype=int)
#np.ones((3,5),dtype=float)
# Create an array filled with a linear sequence
 # Starting at 0, ending at 20, stepping by 2
 # (this is similar to the built-in range() function)
# np.arange(0, 20, 2)
# Create an array of five values evenly spaced between 0 and 1
#np.linspace(2,5,5)
#np.random.random((3, 3))

x1 = np.random.randint(10, size=6) # One-dimensional array
x2 = np.random.randint(10, size=(3, 4)) # Two-dimensional array
x3 = np.random.randint(10, size=(3, 4, 5)) # Three-dimensional array
x1
x2
x3