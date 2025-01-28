nterm=int(input("enter a number: "))
result=list(map(lambda x : 2** x, range(nterm+1)))

for i in range(1,nterm+1):
    print("the value of 2 raised to power of ",i,"is",result[i])