# # qube of num = add of all qube 
# ex: 153 = 1^3 + 5^3 + 3^3
#         = 1   + 125  + 81
#         = 153

num = int (input("ENter a num:"))
sum = 0
temp = num
while temp >0:
    digit = temp%10
    cub= digit**3
    sum = sum+ cub
    temp //=10

if sum == num:
    print("it is armstrong num")
else:
    print("not armstong")