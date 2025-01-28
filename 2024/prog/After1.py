# Write a Python program to reverse those strings which contain no alphabets and others convert to uppercase.

# Original list:
# ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '@#$$$%^']
# Reverse the case of all strings. For those strings which contain no letters, reverse the strings:
# ['CAT', 'ABCDEFHIJKLMNOP', '52421', '', 'FOO', 'UNIQUE', '@#$$$%^']
# has context menu

class StringProcessor:
    def __init__(self, string_list):
        self.string_list = string_list

    def process_strings(self):
        result = []
        for char in self.string_list:
            if char.isalpha():
                result.append(char.upper())
            else:
                result.append(char[::-1])
        print(result)

lst =['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '@#$$$%^']
s=StringProcessor(lst)
s.process_strings()


















# l = ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '@#$$$%^']

# r =[]

# for char in (l):
#     if char.isalpha():
#         r.append(char.upper())
#     else:
#         r.append(char[::-1])
    
# print(r)
            
