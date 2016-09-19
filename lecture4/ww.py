"""
test script to show that python breaks out of the function after excuting 'return'
"""
def www(x):
	if x<3:
		return("lsmaller")
	elif x<10:
		print("larger")
	x = x +100
	return(x)
	