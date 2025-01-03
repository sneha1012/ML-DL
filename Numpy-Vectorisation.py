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

#Indexing and slicing

a = np.arange(10)
print(a)

#accesing an element 
print(f"a[2].shape: {a[2].shape} a[2], accesing an element returns a scalar")

#negative index, count from the end
print((f"a[-1] = {a[-1]}"))

#accesing should should be done of indexes within the range otherwise they will rpoduce and error.


