l1=[1,45,35,29,10]

l2=[]
for i in l1:
    if i>30: # condition can be applied
        l2.append(i)
print(l2)
# when u need to copy the elements of one list in another use this rather than above
l3=[i for i in l1]
print(l3)
# to apply condition
l3=[i for i in l1 if i>=25]
print(l3)