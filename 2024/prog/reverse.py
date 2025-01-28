lst = ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique']


r = []
for char in lst:
    if char.isalpha():
        r.append(char[::-1]) 
              
print(r)
