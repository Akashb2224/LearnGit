lst1= [1,2,3,7,9,3,4,7,2,6,8,5,1,4,2,3,7,2,1,4,5,1]

adj_digit= [i for i in lst1 if sum(int(digit)) for digit in str[i] in lst1]

print(adj_digit)
