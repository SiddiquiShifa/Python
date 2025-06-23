# maximum of three nums in python
def maxvalue(v1,v2,v3):
    if v1>v2 and v1>v3:
        print(v1,"---greater number")
    elif(v2>v1 and v2>v3):
        print(v2,"---greater number")
    else:
        print(v3, "---greater number")
    
maxvalue(13,233,56)