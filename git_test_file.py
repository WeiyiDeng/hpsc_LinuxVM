"""
# Hello World program in Python
    
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print x
"""    
"""    
a = 0
b = 2
print(a + b)

a = "0"
b = "2"
print(a + b)

a = "0"
b = 2
print(int(a) + b)
print(a + str(b))
print(float(a) + b)
"""
"""
# if syntax
a = 20
if a >= 22:
    print("if")
elif a >= 21:
    print("elif")
else:
    print("else")
    
def greater_less_equal_5(ans):
    if ans > 5:
        return 1
    elif ans < 5:          
        return -1
    else:
        return 0
        
print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)    
"""    
def gut_test():
    print "Time for your gut test!"
    print "Do you choose left or right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "HaHa"
    elif answer == "right" or answer == "r":
        print "YOU LOSS"
    else:
        print "You didn't pick left or right! Try again."
gut_test()
"""
def clinic():
    print "You've just entered the clinic!"
    print "Do you take the door on the left or the right?"
    answer = raw_input("Type left or right and hit 'Enter'.").lower()
    if answer == "left" or answer == "l":
        print "This is the Verbal Abuse Room, you heap of parrot droppings!"
    elif answer == "right" or answer == "r":
        print "Of course this is the Argument Room, I've told you that already!"
    else:
        print "You didn't pick left or right! Try again."
        clinic()

clinic()
"""
    
    
    
    
    
    
    
    
    
    