"""
w: module conatining a function of ln
"""
"""
s = 0.01                          # inital guess
x = 4                   
"""
from numpy import *        # import all necessary funs from numpy
max_k = 100                       # maximum number of iterations
tol = 1.e-14                         # tolerance set to 1*10^-14

def myln(s,x):
	for k in range(max_k):
		print("before %s interations, s = %20.15f" %(k+1,s))      # %s is the location to insert the content after %
		# can change format too; %20.15f is for printing 20 digits with 15 digits after decimal in fixed point notation 
		s_prev = s
		s = s - 1 + x/exp(s)
		delta_s = abs(s-s_prev)
		if delta_s < tol:
			break
		
	print("\nafter %s interations, s = %s") %(k+1,s)
