#approch1 using temp variable
mylist=[1,2,3,4,55,77,99]
temp=0
size=len(mylist)
print("list before swapping:",mylist)
temp=mylist[0]
mylist[0]=mylist[-1]
mylist[-1]=temp

print("list after swapping:",mylist)
# ///////////////////////////////////////////////////////////////////////////
#Approch2 
mylist1=[1,2,3,4,55,77,99]
mylist1[0],mylist1[-1]=mylist1[-1],mylist1[0]
print("list after swapping approch2:",mylist1)
# ////////////////////////////////////////////////////////////////////////////
#approch 3 using tuple variable
mylist2=[1,2,3,4,55,77,99]
get=(mylist2[0],mylist2[-1])        #tupple packing

mylist2[-1],mylist2[0]=get          #tupple unpacking
print("list after swapping approch3:",mylist2)
# ////////////////////////////////////////////////////////////////////////////

#approch 4 using * operand
mylist3=[11,2,3,4,55,77,66]
start,*middle,end=mylist3
mylist3=end,*middle,start
print("list after swapping approch4:",mylist3)
# ////////////////////////////////////////////////////////////////////////////////

#approch5 using pop() function
plist=[00,2,3,4,55,77,11]
first=plist.pop(0)
print(first)
last=plist.pop(-1)
print(last)
plist.insert(0,last)
plist.append(first)

print("list after swapping approch5:",plist)
