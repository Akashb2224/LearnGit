# Original list
lst = ['cat', 'abcdefhijklmnop', '12425', '', 'foo', 'unique', '@#$$$%^']

# Result list
result = []

# Iterate through each element in the list
for char in lst:
    if char.isalpha():
        result.append(char.upper())  # Convert to uppercase if it contains alphabetic characters
    else:
        result.append(char[::-1])    # Reverse the string if it contains no alphabetic characters

print(result)  # Output the result      #['CAT', 'ABCDEFHIJKLMNOP', '52421', '', 'FOO', 'UNIQUE', '^%$$$#@']


