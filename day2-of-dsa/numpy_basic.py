import numpy

#  basic array
arr=numpy.array([1,2])

print(arr)

#  2d array
arr2=numpy.array([[1,2],["mukesh","rohit"]])
print(arr2)

#  in case array is not of equal length will raise error 
# arr3=numpy.array([[1,2,3],["mukesh","rohit"]])
# print(arr3)
# ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (2,) + inhomogeneous part.
print(sum(arr))

# access 1st array 
print(arr2[0])

#  access 1st element of 2nd array 
print(arr2[1][0])


#  slicling numpy
print(arr2[0:2])

