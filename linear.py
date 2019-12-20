#linear algebraic operations
import numpy as np
a=input("Enter the 2nd matrix:")
b=input("Enter the 2nd matrix:")
x=np.array(a)
y=np.array(b)
print("matrix algebraic operations")
a=[x,y,np.add(x,y),np.subtract(x,y),np.dot(x,y),np.divide(x,y),np.transpose(x),np.transpose(y),np.linalg.det(x),np.linalg.det(y),np.linalg.inv(x),np.linalg.inv(y),np.linalg.eigvals(x),np.linalg.eigvals(y),np.trace(x),np.trace(y),np.linalg.matrix_rank(x),np.linalg.matrix_rank(y)]
b=["matrix1","matrix2","addition","substraction","multiplication","division","transpose of x","transpose of y","determinant of x","determinant of y","inverse of x","inverse of y","eigen value of x","eigen value of y","trace of x","trace of y","rank of x","rank of y"]
l=len(a)
for i in range(l):
	print np.array(a[i])," -----",np.array(b[i])
	
