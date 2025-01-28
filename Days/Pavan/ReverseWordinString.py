str="welcome to python"
print("Oringinal String ",str)
mystr=str.split()

mystr=mystr[::-1]

print("Reversed String ",mystr)

mystr=" ".join(reversed(mystr))
print("Again Reversed string: ",mystr)