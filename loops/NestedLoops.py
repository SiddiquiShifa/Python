for i in range(1,4): #no.of rows
    for j in range(1,11): #no.of columns
        print(j, end=",")
    print()

for i in range(1,5):
    for j in range(1,i+1): #i+1 is for incrementing as each row is incrementing one cplumn
        print(j, end="")
    print()

for q in range(1,101,10):
    print(q)

# Printing common multiples of 8  n 12
for i in range(1,101):
    if i%8==0 & i%12==0:
        print(i)
