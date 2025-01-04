import numpy as np
import matplotlib.pyplot as plt

##Sigmoif function maps all predicted y output labels between the value of 0 and 1, basically gives u an idea of what is the probability of it to be 1/yes/true (subjective to mapping)
#We try to map the curve -value to +value with a sigmoid fucntion curve, having horizontal axis as 'z'
#NumPy has a function called exp(), which offers a convenient way to calculate the exponential ( e^z) of all elements in the input array (z).

# Input is an array. 
input_array = np.array([1,2,3])
exp_array = np.exp(input_array)

print("Input to exp:", input_array)
print("Output of exp:", exp_array)

# Input is a single number
input_val = 1  
exp_val = np.exp(input_val)

print("Input to exp:", input_val)
print("Output of exp:", exp_val)