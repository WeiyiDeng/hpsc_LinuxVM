from numpy import *       # import all necessary funs from numpy

s = 0.01                             # inital guess
x = 4                   
max_k = 100                      # maximum number of iterations
tol = 1.e-14                         # tolerance set to 1*10^-14

for k in range(max_k):
	print("before %s interations, s = %s" %(k+1,s))      # %s is the location to insert the content after %
	s_prev = s
	s = 0.5*(s+x/s)
	delta_s = abs(s-s_prev)
	if delta_s < tol:
		break
	
print("\nafter %s interations, s = %s") %(k+1,s)
