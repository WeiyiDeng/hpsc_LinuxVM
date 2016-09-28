x = 3
# x = "three"
y = -22

def ff(z):
	x = z+10
	import pdb; pdb.set_trace()     # import pdb then call set_trace function from pdb
	return(x)             

y = ff(x)

print(x)      
print(y)      