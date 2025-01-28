# using for loop 
# num= int(input("Enter a number: "))
print("numbers divisible by 13 are :")
for i in range(1,100):
    if i%13==0:
        print(i)

# Using anonymus function
l=[39,48,98,53,87,33,65]
result=list(filter(lambda x : x%13==0,l))
print(result)