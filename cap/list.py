l = [20,66,1,5,11,20,11]
dict = {}

for num in l:
    if num in dict:
        dict[num] += 1
    
    else:
        dict[num] = 1
print(dict)


# a = 2
# num1 = l[:a]

# l = l[a:]

# lis = l + num1

# print(lis)