class Myclass:    #class
    def myfun(self):
        pass
    def display(self,name):
        print(name)

m1=Myclass()            # object
m2=Myclass()

m1.myfun()

m2.display("John")

#type of methods intance method , static method
#example2
class myclass1:
    def m1(self):                           #self consider as invoke class in instance method
        print("this is intance method")
    @staticmethod
    def m2(self):                           #self considered as parameter in static method
        print("this is static method")

mc=myclass1()
mc.m1()
mc.m2("hello")
myclass1.m2(20)                              # using class we can access static method

# Example 3
class newclass:
    a,b=10,20                               #class variables
    def add(self):
        print(self.a+self.b)
    def mul(self):
        print(self.a*self.b)

nc=newclass()
nc.add()
nc.mul()

#example 4
i,j=15,25                           #global variable
class aclass:
    x,y=35,45                       #class variables
    def add(self,p,q):              #local variables
        print(p+q)  
        print(self.x+self.y)
        print(i+j)

ac=aclass()
ac.add(55,65)

#example 5
a,b=151,252
class bclass:
    a,b=101,201
    def add(self,a,b):
        print(a+b)                              #access local variable
        print(self.a+self.b)                    #access class variable
        print(globals()['a']+globals()['b'])        #access global  variable
        

bc=bclass()
bc.add(100,200)

#example  create multiple object using same class
class mulobj:
    def display(self,name):
        print("this is display method")
        print(name)

obj1=mulobj()
obj1.display('john')
obj2=mulobj()
obj2.display('wick')


#constructor

class cons:
    def __init__(self):
        print("this is constructor")

    def m1(self):
        print("hello")

mc=cons()       #invoke constructor automatically
mc.m1()


#prametric constructor

class paracons:
    name="Domnick"
    def __init__(self,name):
        print(name)
        print(self.name)

pc=paracons("toreto")


#exapmle

class emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid                    #class variable we can create using self.variable
        self.ename=ename
        self.sal=sal
    def display(self):
        print(self.eid,self.ename,self.sal)

emp=emp(101,"john",30000)
emp.display()


#Example 2nd type =string constructor

class emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid                    #class variable we can create using self.variable
        self.ename=ename
        self.sal=sal
    def __str__(self):                  #string constructor 
        return(self.ename)
e1=emp(101,"john",30000)
print(e1)

