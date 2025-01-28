# list is a collection which is ordered and changable
List1=[10,20,30]
List2=['a','b','d']
List3=["my",10,2,'a']

print(List1)
print(List2)
print(List3)
print(List3[2])
print(List2[-2])
print(List1[1:4])

#change item value

List1[0]=40
print(List1)


#append() , insert()

list=['apple','bannana','cherry']

print(list)

list.append('orange')
print(list)

list.insert(0,'mango')
print(list)

#remove item from list pop(), del, clear()

list.pop(0)
print(list)

del list[3]
print(list)

list.clear()
print(list)

#copy of list list(), copy()

mylist1=['table','chair']
mylist2=mylist1
print(mylist2)

mylist3=mylist2.copy()
print(mylist3)


#joining of list, +, for loop, extend()

jlist1=['a','b','c']
jlist2=[1,2,3]
jlist3=jlist1+jlist2
print(jlist3)

for i in jlist2:
    jlist1.append(i)
print(jlist1)

mylist3.extend(jlist1)
print(mylist3)