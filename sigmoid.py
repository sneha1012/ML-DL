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

def sigmoid(z):
    """
    Compute the sigmoid of z

    Args:
        z (ndarray): A scalar, numpy array of any size.

    Returns:
        g (ndarray): sigmoid(z), with the same shape as z
         
    """

    g = 1/(1+np.exp(-z))
   
    return g

z_tmp = np.arange(-10,11) #create arrange of values within a range, in an order


# Use the function implemented above to get the sigmoid values
y = sigmoid(z_tmp)

# Code for pretty printing the two arrays next to each other
np.set_printoptions(precision=3) 
print("Input (z), Output (sigmoid(z))")
print(np.c_[z_tmp, y])     #np.c is used for column wise concatenation for two arrays earlier.

##logistic regression is an algorithm used for classification with categorical value, for example if the tumour is malignant or not, email is spammed category or not or anything else ha two options.
#we need to apply the sigmoid function with, logistic regreesion.

x_train = np.array([0., 1, 2, 3, 4, 5])
y_train = np.array([0,  0, 0, 1, 1, 1])  #binary class problem value are 0 and 1

w_in = np.zeros((1))
b_in = 0


