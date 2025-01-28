# Leap year once in 4 year ex. 1996,2000,2004,2008
year=int(input("Enter a year: "))

if year%400==0 and year%100==0:
    print("The given year is leap is",year)
elif year%4==0 and year % 100!=0:
    print("The given year is leap is",year)
else:
    print("The given year in not leap year",year)
