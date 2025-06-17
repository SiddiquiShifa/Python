# local variable
x=21
print(x)
def funct():
    x=23
    print(x)
funct()

a=12
def funct():
    global a
    a=232
    print(a)
funct()
print(a)