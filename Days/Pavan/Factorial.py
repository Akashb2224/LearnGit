# Approch 1
num=1
factorial=1
if num < 0:
    print("factorial of -Ve number is not possible")

if num==0 or num==1:
    print("factorial of :",num ,"is 1")

for i in range(1,num+1):
    factorial=factorial*i

print("factorial of number:",{num},"is",{factorial})


#apprch 2 using reccursion

def factorial(N):
    if N == 0 or N == 1:
        return 1
    else:
        return N * factorial(N - 1)

# Call the function and print the result
N = 5
fact = factorial(N)
print(f"Factorial of {N} is {fact}")
