#if , if...else, elif

# person is eligible for voting or no

age=15
# age=int(input("Enter age"))

if age>=18:
    print("eligible for vote")

else:
    print("not eligible for voting")





#Find number even or odd
num=10

if num%2==0:
    print("Even number")
else:
    print("odd number")



num=11
print("Even number")    if num%2==0  else   print("odd number")

# elif
weekno=4

if weekno==1:
    print("sunday")
elif weekno==2:
    print("Monday")
elif weekno==3:
    print("Tue")
elif weekno==4:
    print("wed")
elif weekno==5:
    print("thur")
elif weekno==6:
    print("friday")
elif weekno==7:
    print("Sat")
else :
    print("Invalid no")


# check no is +ve oe -ve
    
num=-8

if num>=0:
    print("Positive Number")
else:
    print("negative number")

# largest no
    
a, b = 100, 20
if a>=b:
    print(a," = is the largest number")
else:
    print(b," = is the largest number")


# input weekname and print no
weekno=input("Enter week name ")

if weekno=="sunday":
    print("1")
elif weekno=="Monday":
    print("2")
elif weekno=="Tue":
    print("3")
elif weekno=="wed":
    print("4")
elif weekno=="thur":
    print("5")
elif weekno=="friday":
    print("6")
elif weekno=="Sat":
    print("7")
else :
    print("Invalid input")
