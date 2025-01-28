from prog import PrimeNumber 
list_input = [1, 13, 65, 44, 7, 99, 93, 101]

# Create an instance of the PrimeNumbers class
prime_obj = PrimeNumber(list_input)

print("Prime Status of each number:")
for num in list_input:
    print(f"{num}: {prime_obj.PrintPrimeTillLimiter(num)}")

# Call the PrintPrimeFromList method to get all primes in the list
primes = prime_obj.PrintPrimeFromList()
print("\nPrime numbers in the list:")
print(primes)