mytuple=('apple','bannana','cherry')
print(mytuple)
print(mytuple[1])


mytuple1=(1,2,3,4,5,6,7,8)
print(mytuple1[4:9])
print(mytuple1[-4:-1])

#convert tuple to list and changre the value

mylist=list(mytuple)
mylist[0]=("orange")
print(mylist)
mytuple=tuple(mylist)
print(mytuple)

#reading tuple using for loop
for i in mytuple1:
    print(i)

# check item present in tuple
if "orange" in mytuple:
    print("orange is present in mytuple")
else:
    print("orange is not present in mytuple")

print(len(mytuple))

#copy of tuple

mytuple1=mytuple
print(mytuple1)

#delete tuple
# del mytuple1
# print(mytuple1)

#combining/joining of tuple
tuple1=(10,20,30)
tuple2=('a','b','c')
tuple3= tuple1 + tuple2
print(tuple3)