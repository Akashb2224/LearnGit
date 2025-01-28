def duplicate(s):
    dic={}
    dup=[]

    for char in s:
        if char in dic:
            dic[char] +=1
        else:
            dic[char] = 1

    for char,value in dic.items():
        if value > 1:
            dup.append(char)

    print(dic)
    print(dup)


s="programming"

duplicate(s)