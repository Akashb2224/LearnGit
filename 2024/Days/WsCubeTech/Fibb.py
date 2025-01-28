# fibbo is addition of all previous num
n=10
x1=0
x2=1
print(x1)
print(x2)
for i in range(2,n+1):
        x3=x1+x2
        print(x3)
        x1=x2
        x2=x3


