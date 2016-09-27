x = 3
y = 22

def ff(z):
	x = z+3                # x here is local variable in the func
	return(x)              # does not change the value of x in the main program
# to avoid confusion, use a different symbol (eg. u) instead of x in the function

y = ff(x)

print(x)      # run debugtry in ipython, prints out 3
print(y)      # run debugtry in ipython, prints out 6