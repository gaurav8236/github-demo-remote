#Add implementation
def add(x,y):
	return x+y
#Subtract implementation
def subtract(x,y):
	return x-y               #on master branch
#Multiply implementation
def multiply(x,y):
	return x*y         #on Bug01 branch
#Divide implementation
def divide(x,y):

	if y==0:        # on master branch
                return Divide_by_0_Error
        else:
                return x/y
