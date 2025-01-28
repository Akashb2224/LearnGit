# Approch 1 using while loop
num= int (input("Enter a num: "))
if num<0:
    print("Enter Positive number")
else:
    sum=0
    while num>0:
        sum+=num
        num-=1

    print(sum)



# Approch 2 using for loop
num= int (input("Enter a num: "))
if num<0:
    print("Enter Positive number")
else:
    sum=0
    for i in range(1,num+1):
        sum+=num
        num-=1

    print(sum)