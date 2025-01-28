#Approch 1 using 3rd variable
A = 10 
B= 20
print("Before swapping:",A,B)
temp =10
A = B
B=temp
print("After Swapping:",A,B)


#Approch 2

C,D = 30,40
print("Before swapping:",C,D)
C,D = D,C                   #RHS tupple packing LHS tupple unpacking
print("After Swapping:",C,D)