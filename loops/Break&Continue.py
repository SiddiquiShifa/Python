
# Here except 5 eveery number would be printed
for i in range (1,10+1):
    if i==5:
        continue
    else:
        print(i)

# If we want not to print after 7 numbers will use BREAK and if the num is before 7 it will print it 
for i in range(1,11,1):
    if i==7:
        break
    else:
        print(i)