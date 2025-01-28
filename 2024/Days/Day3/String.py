s="welcome"
s='a'
s=str("hello")


print(id(s))        #2751174562736
s='D'
print(id(s))        #140718600469352    since strings are immutable


# concatination string
a="hello"
print(a +"python")
print(a*2)

# Slicing
name="AKASh Basagare"
print(name[0:6])        #AKASh

rev=(name[::-1])       
print("revers",rev)              #eragasaB hSAKA

first , last= rev.split()
print(last+" " +first)      #hSAKA eragasaB

for i in rev:
    blank=""
    if i.isupper():
        balnk=i.lower()
    else:
        balnk=i.upper()
print(blank)
print("completed")


# slicing operator

Str="welcome"
last=(Str[3:])
first=(Str[:3])
print(last,first)




# ord() ascii character   chr()

print(ord("x"))

print(chr(120))

# max(), min(), len()

print(max("abc"))
print(min("abc"))
print(len("abc"))

# in, not in operator

s="hello python"
print("python" in s)
print("java" in s)

print("python" not in s)
print("java" not in s)

#testing string
print("Testing String")
s= "welcome to python"
print(s.isalnum())

print("python".isalpha())

print("2012".isdigit())

print("is".isidentifier())

print(s.islower())

print("WELCOME".isupper())

print(" ".isspace())

print(s.find("to"))

print(s.count("t"))

print(s.capitalize())

print(s.title())

print(s.lower())

print(s.swapcase())

print(s.replace("to","in"))


#reverse string

n="akash"
rev=""
for i in n[:-1]:
    rev=n+rev

print("reverse of string is " ,rev)