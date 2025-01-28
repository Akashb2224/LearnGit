# Approch 1 fibonacci 0,1,1,2,3,5

s1=0
s2=1
print(s1)
print(s2)

for I in range(2,11):
    sum= s1+s2
    print(sum)
    s1=s2
    s2=sum