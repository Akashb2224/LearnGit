def fact(n):
    if n < 0:
        print("Factorial of a negative number does not exist")
        return None
    elif n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = 5
result = fact(num)
if result is not None:
    print(f"The factorial of {num} is {result}")



