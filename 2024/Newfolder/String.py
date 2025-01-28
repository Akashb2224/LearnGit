strining1 = "ApplesAndOranges"
vo = "aeiou"

str=strining1.lower()

print(str)

for char in str:
    if char in vo:
        print(char)