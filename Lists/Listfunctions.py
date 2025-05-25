# a=["Sara","John","Aaron","Nario","Zaie","Sara"]
# print(a)
# # Find length
# print(len(a))

# # # Ocurence of particular element
# print(a.count("Sara"))

# # add into list
# a.append("Anne")
# print(a)

# # # add element ata specific location
# a.insert (1,"Varon")
# print(a)

# # to remove at particular index
# a.pop(2)
# print(a)
# print(a.pop(3)) # the one which is removed that particular would printed
# # to remove
# a.remove("Sara")
# print(a)

# # to create  a copy of list
# b=a.copy()
# print(b)

# # to access an element
# print(a.index("Sara"))
# print(a[1])

# # To extend a list
# c=["Sabrina"]
# a.extend(c)
# print(a)

# # 
# # a=[3]
# # b=[1]
# # c=a+b
# # print(c)

# # # sum
a=[2,1,4,2]
# # c=sum(a)
# # print("sum  of ",a,"is :",c)
# # using for loop
# for i in a:
#     print(sum(a))
#     break # mentioned it to print only once

# # another method
# total=0
# for i in a:
#     total+=i
# print(total)

# # reverse without using fun reverse
# a=a[::-1]
# print(a)

# # largest n smalles num
# print(max(a))
# print(min(a))

# # count occurence
# # first method
# # print(a.count(2))
occur=0
for i in a:
    if i==2:
        occur+=1
print(i,"occured",occur,"times")

# check if list is palindrome
a=[1,2,1]
c=a[::-1]
if a==c:
    print("Yes its palindrome",a,c)
else:
    print("Its not",a,c)
    
# to reverse the lsit
a=[1,2,"Saea"]
a.reverse()
print(a)

# to sort the list 
a=['sa','aa','as']
a.sort()
print(a)
a=[1,6,2,99,21]
a.sort()
print(a)

# empty the list
a.clear()
print(a)