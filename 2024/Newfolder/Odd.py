#squre even , 
list2 = [2,4,6,3,9,13]
sq=[]
cub=[]
for i in list2:
    if (i % 2== 0):
        sq.append(i**2)        

        print (sq)
    else:
        cub.append(i**3)
        print(cub)
print ("even numver squareis :",sq)
print ("Odd number cube is :",cub)