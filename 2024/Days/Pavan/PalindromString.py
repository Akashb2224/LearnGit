#Approch 1 using slicing 
str="madam"

if str[::-1]==str:
    print("string is Palindrom",str)

else:
    print("string is not Palindrom",str)


#Approch2 using reverse() method

str1="madam"

reverse="".join(reversed(str1))
if str1==reverse:
    print("string is palindrom",str1)

else:
    print("string is not Plaindrom",str1)