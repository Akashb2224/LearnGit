print("this is starting of program")
print("this is starting of program")
print("this is starting of program")
try:
    print(x)
except:
    print("exeption occurs")
print("this is ending of program")
print("this is ending of program")
print("this is ending of program")


#example 2

print("this is example 2")
print("program is in progress")
try:
    print(10/5)
except  ZeroDivisionError:
    print("exeption occured and handled")
print("program completed")


#example 3 multiple except block

print("this is example 3")
try:
    a,b=10,5
    res=a/b
    print("Result is ",res)
except  ZeroDivisionError:
    print("thrown  ZeroDivisionError exception")
except SyntaxError:
    print("trown Syntax error exception")
except:
    print("Exception handled")
else:
    print("no exception occured")
finally:
    print("this finally block always execute")


#Raising our own exception
print('Raising our own exception')
def enterage(age):
    if age <0:
        raise ValueError("only integers are allowed")
    if age%2==0:
        print('age is even')
    else:
        print('age is odd')



age=-1
try:
    enterage(age)
except ValueError:
    print('Value error exception is handled')
print('program completed')