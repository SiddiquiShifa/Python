# # variables datatypes typecasting input

# print("Hello world")
# a=7

# print(type(a))
# print(a)
# b=4
# print(a+b)

# Ad=input("Enter input")
# print(Ad)

# # comment
# exp=eval(input("Enter any equation here:"))
# print(exp)

# # write a program to swap two variables
# # method1

x=1
y=2
# temp=x
# print(temp)
y=x
print("value of y",y)

# method 2
z=90
e=28
e,z=z,e
print(e)
print(z)

#program tp convert float into integer
variable=12.4
print(type(variable))

variable=int(variable)
print(type(variable))

# write a program to take details from a studentfor id cardand then print it in different lines

print("Data for student id")
name=input("Enter name :")
grade=input("Enter grade : ")
age=int(input("Enter age"))
print(name+ "\n" +grade)
# also
print(f"{name } And\n {grade}")

# program to  take inpu from user and convert it type

c=int(input("Enter an int no.: "))
print(type(c))
c=float(c)
print(c,type(c))