# Approch 1 
num=10
count = 0

for i in range(1,num+1):
    if(i%2==0):
        count = count + 1
    
if count==2:
    print("number is prime")
else:
    print("Number is not Prime")

