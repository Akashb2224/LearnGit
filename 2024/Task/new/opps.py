# OOPS
# class and instance variable
# file operations for a csv file
# list comprehension

lst=[1,2,3,4,5]
lst1=[4,5,6,7]

# add_lst=[a+b for a,b in zip (lst[1:],lst1)]
# print(add_lst)

lst3=[]
for i in lst:
    if i==1:
        continue
        
    for j in lst1:
        lst3.append(i+j)

print(lst3)
