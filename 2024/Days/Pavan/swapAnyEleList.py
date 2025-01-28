# Approch 1
print("this is Approch1")
import random
mylist=[random.randint(0,101) for i in range(6)]
print("list befor swaping",mylist)
pos1,pos2=1,3
mylist[pos1],mylist[pos2]=  mylist[pos2],mylist[pos1]
print("list after swapping",mylist)


#approch2
# swap position5,pos6 to pos1,pos2
lst=[11,22,33,44,55,66]

temp=lst[-1],lst[-2]                #tupple packing
lst[-1],lst[-2]=lst[0],lst[1]   
lst[0],lst[1]=temp                  #tupple unpacking

print(lst)