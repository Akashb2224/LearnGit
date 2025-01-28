# Prime num divede by itself
A= int(input("Enter A number: "))
# A= 10
if A==1:
    print("It is not Prime Number: ",A)
count=0
for i in range(1,A):
    if A%i==0:
        count+=1
if count==1:
    print("The given Number is Prime :",A)
else:
    print("The Given Number is not Prime: ",A)