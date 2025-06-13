# find max & min in a set
a={1,23, 21,34,67}
print("maximum:",max(a))
print("minimum",min(a))

# find common elemnt in three lists using sets
a=[1,2,3,4,5]
b=[1,21,2,43,5]
c=[1,4,3,5,2]
print("common elements :",set(a)&set(b)&set(b)) #converted into data type

# find difference between two sets
a={1,203, 21,3,67}
b={1,4, 2,34,67}
print(a.difference(b))

# remove an item from set
a={1,203, 21,3,67}
a.remove(1)
print(a)
print(len(a))

#  Safe Remove Task: Try to remove 400 safely without throwing an error.
z = {100, 200, 300}
z.discard(400)
print(z,"No error even if discarded 400 as we used \"discard\"")
z.remove(400)
print(z,"ERRORRRRRRRRR")


