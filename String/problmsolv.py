# #   prime nnum 1,3,5
# num=int(input("Enter num: "))
# if num<=1:
#     print("Its Not a prime number")
# else:
#     for i in range(2,num):
#         if num%i==0:
#             print("is not prime")
#             break
#     else:
#             print("Its  Prime")

# # palindrome
# word = input("Enter a word: ")

# if word == word[::-1]:
#     print("It's a palindrome!")
# else:
#     print("Not a palindrome.")

# # num palindrome
# num = input("Enter a number: ")

# if num == num[::-1]:
#     print("It's a palindrome number!")
# else:
#     print("Not a palindrome.")

# # Write a program for the string appear as in comma seprated 
# a="ootd.summer.cool.yum."
# print(a.split('.'))

# # write a program to sort strings alphabetically
# a=input("Enter to sort alphabetically :")
# print(sorted(a))

# # write a program to remove a charater
# a="hello"
# print(a)
# rp=(input("Which letter you want to replace :"))
# c=a.replace(rp,"")
# print(c)

# # remove comma seprated into single word
# a="f.r.i.e.n.d"
# print(a)
# print(a.replace('.',""))

# # count a  number of time a substring occurs
# a="She sells the seashell on the seashore"
# print(a)
# sub=(input("Which substring you want to count? "))
# print(a.count(sub))

# # userinput reverse it
# a=input("Enter a string to reverse: ")
# print(a[::-1])

# # program to check if input consists only digits
# a=(input("Enter a string to check if its digit: "))
# print(a.isdigit())

# # write a program to check if string is palindrome
# a=input("Enter string to check if its palindrome: ")
# b=a[::-1]
# if a==b:
#     print("Yes itsa palindrome.")
# else:
#     print("Nope")

# Write a program to find num of vowels in string
a=input("Enter string to check no. of vowels in it : ")
b='aeiouAeiou'
vowels=0
# u can use anyword in place of char for i in a...
for char in a:
    if char in b:
        vowels+=1
else:
    print("It dosnt consists vowels")

print("Number of vowels in string:",vowels)

# write a program to check if every word in string starts with capital letter
a=input("Enter string : ")
print(a.istitle())