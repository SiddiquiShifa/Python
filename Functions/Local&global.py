
x=21 #global variable
print(x)

def funct():
    x=23 #local variable declared inside teh function
    print(x)
funct()
print(x) # will print global a value

print()
print("Global")
a=12
print(a)
def funct():
    global a
    a=232
    print(a)
   
funct()
print(a)
a=4
print(a)