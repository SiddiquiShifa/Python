
# # Sum of all even num upto 50
# sum=0
# for i in range(1,51):
#     if i%2==0:
#         sum+=i
# print(sum)

# # Program to write number and their squared nums
# for i in range(1,10+1):
#     print(i)
#     print("Its square is : ",i**2)

# # Program to find sum of first ten odd num using while loop
# sum=0
# i=1
# while i<=20:
#     if i%2!=0:
#          sum+=i
         
#     i+=1
# print(sum)

# # Program to check if a num is divisble by 8 and 12 upto 100
# for i in range(1,100+1):
#      if i%8==0 and i%12==0:
#           print(i)
#      i+=1

# # Billing system 
# while True:
#     name=input("Enter name of cutomer : ")
#     total=0
#     while True:
        
#         amount=float(input("Enter amount: "))
#         quantity=int(input("Enter Quantity: "))
        
#         ask=input("Done? : ")
#         if ask=="yes":
#             break
#     total=amount*quantity
#     print(total)
#     break

# # another method

# while True:
#     name=input("Enter name of cutomer : ")
#     total=0
#     while True:
        
#         amount=float(input("Enter amount: "))
#         quantity=int(input("Enter Quantity: "))
#         total+=amount*quantity
#         repeat=input("Do you want to add more items? : ")
#         if repeat=="no":
#             break
#     print("-"*30)
#     print("Name : ",name)
#     print("Amount to be paid : ",total)
#     print("-"*30)
#     print("*******Happy Shopping*******")
#     break

# a="Why fit in ,  When you are born to standout!"
# # Find length
# print(len(a))

# # how many times letter o is occureing
# print(a.count("o"))

# # Convert in upper lower case
# print(a.lower())
# print(a.upper())

# # in Title
# print(a.title())

# # Find index number of "fit in"
# print(a.find("fit in"))

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end="")
#     print()


# for i in range(1,6):#rows
#     for j in range(6,i,-1):#columns
#         print(i,end="")
#     print()

print()
print("Right triangle") 
for i in range(1,6):
    for j in range(5,i,-1):
        print(i,end=" ")
    for k in range(i):
        print("*",end=" ")
    print()

for i in range(1,6): 
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(4,0,-1):
    for j in range(i,0,-1):
        print("*", end=" ")
    print()

    
for i in range(1,11):
    for j in range(1,i+1):
        print(i*j,end=" ")
    print()

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()