str="welcome"
dic={}

for char in str:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1
print(dic)