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
    print("Hey m,y name is:",name[1]) #can chanfe the values to call as per requiremnet
arbitrary("Lisa","Hanna","Raye")


# return stmt
def returnstmt():
    return("Hellp World")
print(returnstmt()) # need to write print (.......())
def add(a,b):
    return("Addition=",a+b,"Subtracion=",a-b)
print(add(12,34))

def add (a,b):
    return(a+b)

result=add(31,23)
print(result)
if result>10:
    print(result,"is greater than 10")
    print("able to use the result of function bcoz of return stmt")
    print()

def add(a, b):
    c = a + b

result = add(5, 3)
print(result,",Returns none coz inside function no return stmt ")

# # recursion
# def hello():
#     print("hello")
#     return(hello())
# print(hello()) # this would loop for limit-993 times

def fact(n):
    if n==1:
        return 1
    else:
        return (n*fact (n-1)) # deep...fact(n-1) --->CONCEPTUAL
print(fact(5))

# Lambda function
lambdaFunc= lambda b: b+10
print(lambdaFunc(2))

# only one expression
lambdaFunc= lambda a,b,c: (a*b)+c #one expression
print(lambdaFunc(12,13,14))

# # cannot be like this
# lambdaFunc=lambda a,b: a*b, a+b # you make it one exp by (a*b,a+b)
# print(lambdaFunc(12,12))

