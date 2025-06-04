# sort  a dictionary by value
a={"b":1,"c":2,"d":3,"e":4}
sorted_dict=sorted(a.values())
print(sorted_dict)


a={}
for x in range(1,6):
    key=int(input("Enter num : "))
    value=key**2
    a[key] = value                 # store in dictionary
print(a)
    
    # value = input("Enter value: ") # u can take values a s input like this

# print  a dict where keys are numbers between 1 to 15 values sqaure of keys

