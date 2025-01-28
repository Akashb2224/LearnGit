# factorial is product of all previus num
num = int(input("Enter a num: "))
fact=1
if num<0:
    print("Factorial og negative num is does not exist")
elif num==0:
    print("factorial of 0 is 1")
elif num>0:
    for i in range(1,num+1):
        fact =fact *i

print(fact)