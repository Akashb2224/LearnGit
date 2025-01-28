def show (n):
    if(n==0):           #base case
        return
    print(n)
    show(n-1)

show(5)

#factorial
def fact(n):
    if(n==1 or n==0):
        return 1
    return fact(n-1) * n

print("Factorial of nummber n: ", fact(5))

#sum of n number
def cal_sum(n):
    if (n==0):
        return 0
    return  cal_sum(n-1) +n

sum=cal_sum(5)
print("sum of number: ", sum)

#print all element in list2
def print_list(list,idx=0):
    if (idx==len(list)):        #base case
        return
    print(list[idx])
    print_list(list,idx+1)

fruit= ["mango","bannana","apple"]
print_list(fruit)