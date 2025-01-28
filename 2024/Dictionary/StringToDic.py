user=input("Enter a string")
words=user.split()
d={}
for i in words:
    ch=i[0]
    v=i[1]
    d=ch,v


print(d)