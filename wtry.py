from numpy import *       # import all necessary funs from numpy

s = 1
x = 4
for i in range(3):
	s = 0.5*(s+x/s)
	
print(s)
