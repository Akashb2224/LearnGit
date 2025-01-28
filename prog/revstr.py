# Write a Python program to reverse those strings which contain no alphabets and others convert to uppercase.

# Original list:
# ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '@#$$$%^']
# Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
# ['CAT', 'ABCDEFHIJKLMNOP', '52421', '', 'FOO', 'UNIQUE', '@#$$$%^']
# has context menu

lst = ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique']

# def reverse_convert(lst):
#     r = []
#     for char in lst:
#         if char.isalpha():
#             r.append(char.capitalize)
#     else:
#         r.append(char[::-1])        
#     return r


r = []
for char in lst:
    if char.isalpha():
        r.append(char.upper())
    else:
        r.append(char[::-1])        
print(r)




lst = ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique']