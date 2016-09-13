from numpy import *       # import all necessary funs from numpy

s = 1
x = 4
for k in range(6):
	print("before %s interations, s = %s" %(k+1,s))      # %s is the location to insert the content after %
	s = 0.5*(s+x/s)
	
print("\nafter %s interations, s = %s") %(k+1,s)
