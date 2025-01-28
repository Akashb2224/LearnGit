lst=[4, 1, 3, 4, 3, 1, 3, 2, 3, 3, 3, 8, 7]

dict={}

for i in (lst):
    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1

print(dict)