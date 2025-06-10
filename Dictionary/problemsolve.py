# sort  a dictionary by value
adict={"b":6,"c":2,"d":3,"e":4}
# sorted_dict=sorted(a.values())
# print(sorted_dict)


# a={}
# for x in range(1,6):
#     key=int(input("Enter num : "))
#     value=key**2
#     a[key] = value                 # store in dictionary
# print(a)
    
    # value = input("Enter value: ") # u can take values a s input like this

# multiply all items in a dictionary
b=1
for x in adict:
    b*=adict[x]
    print(b)

# # Check if a key exists
# d={"name":"Shifa","age":21,"class":"TY"}
# key="age"
# if key in d:
#     print(f"{key} exists with {d[key]}")
# else:
#     print("No")

# Find the key with the maximum value
adict={"b":6,"c":12,"d":3,"e":4}
max_value=max(adict)
print("Key with highes value is:",max_value)


# to get the hoghest value 
d = {"a": 10, "b": 30, "c": 20}
max_value = max(d.values())
print("Maximum value is:", max_value)
