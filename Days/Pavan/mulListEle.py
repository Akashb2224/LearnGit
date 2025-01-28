import random
#Approch 1 using Traversal
mylist=[random.randint(1,6)for i in range(6)]
print(mylist)
result=1

for i in mylist:
    result=result*i

print("Mul of list element is :",result)


#Approch 2 using Numpy package 
print("this is approch 2")
import numpy
mylist2=[1,12,4,4]
print(mylist2)
product=numpy.prod(mylist2)
print("Product/mul of list is :",product)