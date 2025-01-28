#approch 1 using inbuilt function
arr=[-2,-3,101,0,2,3,4,5,67,33,5,78]

arr.sort()
print(arr)
arr.reverse()
print(arr)

print(max(arr))
print(min(arr))

print("second largest",arr[1])


#approch 2 without using inbuilt function
lst=[-2,-3,101,0,2,3,4,5,67,33,5,78]

max= lst[0]
print(max)
n=len(lst)

for i in range(1,n):
    if lst[i] > max:
        max = lst[i]

print(max)
