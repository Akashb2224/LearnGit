#Approch1 using looping statement
mylist=[13,5,23,22,33,55,00,550,331]
ele=100
flag=0
lenth=(len(mylist))

for i in range(1,lenth):
    if mylist[i]==ele:
        print(ele,"element found in list")
        flag=1
        break
if flag==0:
    print(ele,'element not found in the list')

#Approch 2 using in operator
print("this is approch 2")
lst=[1,2,3,4,5,6]
ele=6

if(ele in lst):
    print("element found")
else:
    print("element not found")