def function1():
    print("This is function")
function1() #to call the function

def add():
    a=43
    b=51
    print(a+b)
add()

# parmeteres & args
def add(x,y): #parameters
    print(x+y)
add(12,45) # Arguments
add(3,55)

def rect(length, width):
    print("Area of rectangle is :", length*width)
rect(23,32)

# arbitrary args
def arbitrary(*name):
    print("Hey m,y name is:",name[1])
arbitrary("Lisa","Hanna","Raye")