#Approch 1 using clear() method

mylist=[1,1,122,334,5]
print("Before clearing :",mylist)
mylist.clear()
print("After clearing :",mylist)

#Approch 2 using initialize list with no values
print("this is Approch2")
mlist=[11,2,22,33,4,44]
print("Before clearing :",mlist)
mlist=[]
print("After clearing :",mlist)

#Approch 3 using *
print("this is Approch3")
Arr=[11,22,33,44]
print("Before clearing :",Arr)
Arr *=0
print("After clearing :",Arr)

#Approch 4 using del method
print("this is Approch4")
Alist=[11,22,33,44,55]
print("Before clearing",Alist)
del Alist [:]
print("After clearing",Alist)