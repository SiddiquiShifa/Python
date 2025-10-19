dictData={"name":"Sara", #key : value  pairs
          "age":21,
          "gender":"female"}
print(dictData)
print(dictData["age"]) #can access by key

# Iteration
# printing all the key names
for x in dictData:
    print(x)

# for values
for x in dictData:
    print(dictData[x])#as x is storing keys though writing in [] will provide their values

# using value function
for x in dictData.values():#iterates in its values
    print(x)

# # using item functions (for iterating in both key value)
for x,y in dictData.items():
    print(x,":",y)

# dictionary function
# get
x=dictData.get("name")
print(x)
# print(dictData.get("name"))

# items (tuples form output)
a=dictData.items()
print(a)

# keys
print(dictData.keys())

# values
print(dictData.values())

# copy (same elements of dictionary in another)
d=dictData.copy()
print(d)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# another method using dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

print("\nsetdefault")
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

# The pop() method removes the item with the specified key name:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)

# nested
employee={1:{"name":"Shifa","age":21},
          2:{"name":"Siddiue","city":"Mumbai"}}
print(employee)
print(employee[1])
print(employee[1]["age"])