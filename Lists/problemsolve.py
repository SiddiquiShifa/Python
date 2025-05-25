a=['rose','resa','mone','flao']

# to swap first and fourth element
a[0],a[3]=a[3],a[0]
print(a)

# write a program to add new value into second postion
a.insert(1,"new")
print(a)

# to delete value fromm third position
a.pop(2) #pop is used when u remove using index and "remove"when specifying name of elemnt 
print(a)

# multiply all numbers in the list
b=[2,2,2]
c=1
for i in b:
    c*=i
print(c)

# largest num from list
a=[1,3,6]
print(max(a))