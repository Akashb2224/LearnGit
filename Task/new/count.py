# Define a class counter with a class variable count that keeps track of the number of instances/object created.
#  Each instance declaration should increment this count. 
 
# Create a few instances and print the count.

class Counter:
    # count=0
    def __init__(self):
        self.count+=1

    @classmethod
    def get_count(cls):
        return cls.count
    
obj1= Counter()
obj2= Counter()
print(count)