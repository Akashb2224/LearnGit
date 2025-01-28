#positional , Keywors

def func(i,j):
    print(i,j)

func(10,20)         #positional arguments
func(j=10,i=20)     #keyword arguments

#default values assign to positional arguments

def new(i,j=33):
    print(i,j)

new(100,200)
new(100)


#keyword arguments

def greetings(name,greetmsg):
    print(greetmsg+" "+name)

greetings(name="john",greetmsg="hello")

#combinations of keyword and positional
def my_func(a,b,c):
    print(a,b,c)

my_func(10,20,30)
my_func(a=10,b=20,c=30)
my_func(b=20,c=30,a=10)
my_func(20,30,c=10)


def largest (a,b):
    if a>b:
        return a,b
    else:
        return b,a

res=largest(10,30)
print(res)
print(type(res))