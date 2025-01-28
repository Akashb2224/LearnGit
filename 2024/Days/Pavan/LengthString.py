#Approch 1 using for loop
str="welcome"
count=0

for i in str:
    count+=1

print("lenght of str is :", count)

#Approch 2 using while loop and slicing
print("this is approch 2")
str1="python"
counter=0
while str1[counter:]:
    counter+=1

print("lenght of str is :", counter)

#Approch 3 using len() function
print("this is approch 3")
str3= "java"
lenght=len(str3)
print("lenght of string is :", lenght)

#Approch 4 using len() function
print("this is approch 4")
str4= "Programming"
random="x"
len=random.join(str4).count(random)
print("Length of string is : ",len+1)  # becouse count start from 0