# a=['rose','resa','mone','flao']

# # to swap first and fourth element
# a[0],a[3]=a[3],a[0]
# print(a)

# # write a program to add new value into second postion
# a.insert(1,"new")
# print(a)

# # to delete value fromm third position
# a.pop(2) #pop is used when u remove using index and "remove"when specifying name of elemnt 
# print(a)

# # multiply all numbers in the list
# b=[2,2,2]
# c=1
# for i in b:
#     c*=i
# print(c)

# # largest num from list
# a=[1,3,6]
# print(max(a))

# # smallest value
# print(min(a))

# # ask input to enter 3 names and store into a list
# a=[input("Enter three names :")]
# print(type(a))

# # another methood
# a=[]
# i=0
# while i<3:
#     movie=input("Enter movie name: ")
#     a.append(movie)
#     i+=1

# print(a)

# # Create a list of all even squares between 1 and 50.

# a=[x**2 for x in range(51) if x%2==0]
# print(a)

# Get all vowels from a string
# a="Shifa"

# char="aeiou"
# result=[letter for letter in a if letter in char]
# print(result)

#  Reverse Each Word in a List
a=["Heiba","Sario","John","kaie"]
result=[word[::-1] for word in a ]
print(result)
reverse=a[::-1]
print(reverse)

# Set the values in the new list to upper case:
upper=[x.upper() for x in a ]
print(upper)

# Set all values in the new list to 'hello':
newlist=['hello' for v in a]
print(newlist)
