# set{} is unordered and unindexed

myset={'apple','cherry','bannana'}
print(myset)

#accessing iteam
for i in myset:
    print(i)


print("cherry"in myset)
print("kiwi"in myset)

#add(), update() 

myset.add("orange")
print(myset)
myset.update(["mango",'grapes'])
print(myset)


#nomber of items in set()= len()
print(len(myset))

#remove(),discard(), clear(), del
myset.remove('bannana')
print(myset)


#joining of sets union(), update()
set1={'a','b','c'}
set2={1,2,3}

set3=set1.union(set2)
print(set3)


set4={'x','y','z'}
set4.update(set3)
print(set4)


