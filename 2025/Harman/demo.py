from collections import Counter
str="akash is a good boy,akash is a software engineer.akash is attending harmon interview."
str1=str.replace("."," ").replace(","," ")
str2=str1.split()

# 1st way
# dict={}

# for char in str2:
#     if char in dict:
#         dict[char]+=1
#     else:
#         dict[char]=1

# print(dict)

# 2nd way

counter=Counter(str2)

print(counter)