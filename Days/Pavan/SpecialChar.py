import re
str="welcome~!to#$python$%programming"
str1="welcome to python"

regex=re.compile("[!@#$%^&*()_+~]")

if(regex.search(str1)==None):
    print("No special character present in string")
else:
    print("String contains Special character")