#Approch 1 using looping statement 
mylist= [1,101,10,11,10,12]
ele=10
count=0
l=len(mylist)
for i in range(1,l):
    if mylist[i]==ele:
        count+=1

print(ele,"occurance in list",count,"Times")

#Approch 2 using count() method
print("this is Approch2")
mylist2= [1,101,10,11,10,12,11]
x=122
print("{} has occured {} times ".format(x,mylist2.count(x)))

#Approch 3 using counter() method
from collections import Counter
print("this is Approch3")
mylist3=[11,2,2,22,12,44]
y=2
dix=Counter(mylist3)
print("{} has occured {} times ".format(y,dix[y]))