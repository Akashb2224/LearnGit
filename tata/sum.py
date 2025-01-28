lst=[11,33,22,44,55,66,77,88,99,111]
 
start_ind = lst.index(33)
end_ind=  lst.index(77)

total=sum(lst[:start_ind]+lst[end_ind+1:])

print(total)

