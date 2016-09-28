x = 3
y = 22

def ff(z):
	x = z+3                # x here is local variable in the func
	print("+++ in func ff, x = %s; y = %s; z = %s")   %(x,y,z)          
	return(x)              # does not change the value of x in the main program
# to avoid confusion, use a different symbol (eg. u) instead of x in the function

print("+++ before excuting ff, x = %s; y = %s")   %(x,y)

y = ff(x)

print("+++ after excuting ff, x = %s; y = %s")   %(x,y)      

# in ipython>>> run debugtry.py
# outputs:
# before ff: x = 3, y = 22
# within ff: z = 3, x = 6, y = 22
# after ff: x = 3, y = 6