def is_palindrome(num):
    num = str(num)

    return num == num[:: -1]

try:
    number= int(input("enter num"))

    if is_palindrome(number):
        print("give no is palondrom",number)

    else:
        print("is not palonfrom",number)

except:
    print("plese enter valid int")


