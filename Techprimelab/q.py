# Question 2:

# Input

# x=[4,2,1,3] y =[20,10,30]


# Output

# op = [Null,20,10,30]

# If the multiple of first array element by 10 is available in second show the multiple value in the output array.
# If does not exist than show Null for that




def check(x,y):
    for num in x:
        if num * 10 not in y:
            print("not present")
        else:
            print("present")

x=[4,2,5,1,3,6]
y =[20,10,30,50]

check(x,y)