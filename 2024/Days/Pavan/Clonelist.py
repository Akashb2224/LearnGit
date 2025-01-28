import random
#Approch 1 using slicing technique
mylist=[random.randint(1,10)for i in range(5)]
print("original list is :",mylist)
mylist_copy=mylist[:]
print("copy of list is :",mylist_copy)

#Approch 2 using extend() method
print("this is Approch2")
mylist2=[random.randint(0,100) for i in range(5)]
print("original list is :",mylist2)
mylist2_copy=[]
mylist2_copy.extend(mylist2)
print("After copying list is:", mylist2_copy)

#Approch 3 using List() method
print("this is Approch3")
mylist3=[random.randint(0,100) for i in range(4)]
print("original list is :",mylist3)
mylist3_copy=list(mylist3)
print("After copying list is:", mylist3_copy)

#Approch 4 using copy() method
print("this is Approch4")
mylist4=[random.randint(0,100) for i in range(4)]
print("original list is :",mylist4)
mylist4_copy=mylist4.copy()
print("After copying list is:", mylist4_copy)

#Approch 5 using list comprehesion
print("this is Approch5")
mylist5=[random.randint(0,100) for i in range(4)]
print("original list is :",mylist5)
mylist5_copy=[i for i in mylist5]
print("After copying list is:", mylist5_copy)