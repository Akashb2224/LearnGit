list1 = [43,23,31]

# list1.sort()

# print(list1)

for i in range(list1):
    key=  list1[i]
    j = i -1
    while j >= 0 and key < list1[i]:
        list1 [j + 1] = list [j]
        

