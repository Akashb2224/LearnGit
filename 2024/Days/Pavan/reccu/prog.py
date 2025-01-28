# Create a class "PrimeNumber"
# You should pass "limiter"(positive integer) to its constructor
# It should have 2 methods:
# PrintPrimeTillLimiter(limiter) -> Prints all prime number till limiter
# PrintPrimeFromList() - > Print prime number available in the list

# Create a file "test_prime.py"
# Import the above created class and call both methods from it.

# list_input = [1, 13, 65, 44, 7,  99, 93, 101]

class PrimeNumber:
    def __init__(self,number):
        self.number=number
        
    def PrintPrimeTillLimiter(self,n):
        if n<=1:
            return False
        
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True
    
    def PrintPrimeFromList(self):
        prime= [num for num in self.number if self.PrintPrimeTillLimiter(num)]
        return prime