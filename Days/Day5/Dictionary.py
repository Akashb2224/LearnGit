mydic={101:'x',102:'y',103:'z'}
print(mydic)

#access item/element in dictionary
mydic1={
    "brand":'hundai',
    "model":"i10",
    "year":2022

}

print("print value using key ",mydic1["model"])
print(mydic1["brand"])

#using get()

print(mydic1.get("year"))


#change value

mydic1["year"]=2021
print(mydic1)

#reading dic

for i in mydic1:
    print(mydic1[i])

for i in mydic1.values():
    print(i)

#items() method
for x,y in mydic1.items():
    print("x,y using for loop iteams",x,y)


#check key is present
    
if "brand" in mydic1:
    print("present")
else:
    print("not present")

#find number of items
print(len(mydic1))

#adding/remove items to dictionary

mydic1["colour"]="red"
print("After Adding items",mydic1)

mydic1.pop("colour")
print(mydic1)

del mydic1['year']

print(mydic1)

# del mydic1
# mydic1.clear()
# print(mydic1)


#copy

mydic2=mydic1
print(mydic2)

mydic3=mydic1.copy()
print(mydic3)