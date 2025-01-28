import random
# Approch1 using looping statement
mylist=[random.randint(1,100)for i in range(6)]
print(mylist)
total=0

for i in range(1,len(mylist)):
    total=total+mylist[i]

print("sum of all element frm givenlist is :",total)

# Approch 2 usning sum() method
print("this is approch 2")
mylist1=[random.randint(1,111)for i in range(6)]
print(mylist1)
Total1=sum(mylist1)
print("sum of element of list is :",Total1)