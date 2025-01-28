mylist= ['hi','hello','hi','hello','hi','hi']
L=(len(mylist))
word='hi'
n=4
count=0

for i in range(0,L):
    if (mylist[i]==word):
        count+=1
    if count==n:
        del mylist[i]

print(mylist)

