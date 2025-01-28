user=input("enter String:")
l=user.split()
d={}
for i in l:
    if i not in d.keys():
        d[i]=1
    else:
        d[i]+=1
print(d)

