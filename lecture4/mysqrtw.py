"""
w: module conatining a function of square root
"""
"""
from numpy import *       # import all necessary funs from numpy                 
x = 4                   
"""
max_k = 100                      # maximum number of iterations
tol = 1.e-14                         # tolerance set to 1*10^-14
# s = 0.1                                 # inital guess         # w: cannot set s here, why?

def wsqrt(x, debug=False):          # adds debug flag, default value is false
	from numpy import nan
	s = 1                                  # inital guess
	if x==0:
		return 0                   # python breaks out of the function after 'return'
	elif x<0:
		print("error, x cannot be nonpositive values")
		return nan
	assert x>0 and type(x) is int or float, "unrecognized inputs"
	# w: if assert statement is false, python raises an assertionError message
	
	for k in range(max_k):
		if debug:                       
			print("before %s interations, s = %20.15f" %(k+1,s))      # %s is the location to insert the content after %
		# can change format too; %20.15f is for printing 20 digits with 15 digits after decimal in fixed point notation
		s_prev = s
		s = 0.5*(s+x/s)
		delta_s = s-s_prev
		if abs(delta_s / x) < tol:                # scale by the size of x
			break	
	if debug:		
		print("\nafter %s interations, s = %s") %(k+1,s)
	
	return(s)
