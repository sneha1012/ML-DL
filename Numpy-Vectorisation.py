import numpy as np
import time

#Vectors are ordered arrays of numbers. Denoted in lower case bold letters as x. elemenents of x can be referenced using an index
#Indexing - referring to an element of an array by its psoition within the array
#Slicing - getting  a subset of elements from an array based on their indices.
##vector Creation

a = np.zeros(4);      print(f"np.zeros(4): a = {a}, a data type = {a.dtype}")
a = np.zeros((4, ));  print(f"np.zeros(4,)  a ={a}, a shape = {a.shape}")
a = np.random.random_sample(4); print(f"np.random.random_sample(4): a = {a}, a shape = {a.shape}")

#We can use np.arrange, which creates a evenlenly spaces array using numbers within a specific range.

##1.Indexing

a = np.arange(10)
print(a)

#accesing an element 
print(f"a[2].shape: {a[2].shape} a[2], accesing an element returns a scalar")

#negative index, count from the end
print((f"a[-1] = {a[-1]}"))

#accesing should should be done of indexes within the range otherwise they will rpoduce and error.

##2.Slicing

#Slicing creates an array of indices using a set of three values(start:stop:step). A subest of three also works.

a = np.arange(10)
print(f"a ={a}")

#accesing 5 consecutive elements (start:stop:step)
c = a[2:7:1];  print("a[2:7:1] = ", c)

#aaccess all elements
c = a[:];    print("a[:] =", c)

#access all elements 3 and above
c = a[3:]; print("a[:3] = ",c)


##3.Scalar vector optimisation (multiplying each element in an array by a specific number)
a = np.array([1,2,3,4])

b = 5 * a
print(f"b = 5 * a: {b}")


##4.Vectorisation - Vector Dot Product example (multiplication (.) of two equal sized/shaped matrices)

def my_dot(a,b):
    """ compute the dot product of two vectors
    Args:
    a (ndarray (n, )): input vectors
    b (ndarray (n, )): input vector with same dimensions as a 
    
    Returns:
    v(scalar):
    """

    x = 0 #initializing
    for i in range(a.shape[0]):
        x = x + a[i] * b[i]
    return x

#np.dot
a = np.array([1,2,3,4])
b = np.array([-1,4,3,2])
c = np.dot(a, b)

print(f"Numpy 1-D np.dot(a, b) = {c}, np.dot(a,b).shape = {c.shape}")



