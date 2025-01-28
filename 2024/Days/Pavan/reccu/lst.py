# ["abc", "d", ["ef", "g"], "h"] split 

lst=["abc", "d", ["ef", "g"], "h"]

lst1=[]

for Item in lst:
    for i in Item:
        lst1.append(i)

print(lst1)


