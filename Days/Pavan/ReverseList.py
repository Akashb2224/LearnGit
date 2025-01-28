import  random
#Approch 1 using reverse() methode
mylist=[random.randint(1,100) for i in range(6)]
print("Before reverse list is:",mylist)
mylist.reverse()
print("after reverse list is :",mylist)

#Approch 1 using slicing technique
print("This is Approch 2")
list2=[random.randint(1,100) for i in range(6)]
print("Before reverse list is:",list2)
list2=list2[::-1]
print("after reverse list is :",list2)