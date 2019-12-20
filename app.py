#appending an array
import numpy as np
a=input("Enter 1st array:")
b=input("Enter 2nd array:")
print "A=",a
print "B=",b
c=np.append(a,b)
print("after appending two arrays")
print c
#method2
import numpy as np
a=input("Enter 1st array:")
b=input("Enter 2nd array:")
print "A=",a
print "B=",b
l=len(b)
for i in range(0,l):
	a=np.append(a,b[i])
print("after appending:",a)

