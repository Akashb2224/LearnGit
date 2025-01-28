#single level inheritance
class A:
    def m1(self):
        print("this is m1 method from class A")

class B(A):
    def m2(self):
        print("this is m2 method from class A")

bobj=B()
bobj.m1()           #access m1 method from parent class
bobj.m2()

#multilevel inheritance

print("this is Multilevel inheritance")
class C:
    x,y=100,200
    def c1(self):
        print(self.x+self.y)

class D(C):
    a,b=300,400
    def c2(self):
        print(self.a-self.b)

class E(D):
    i,j=2,5
    def c3(self):
        print(self.i*self.j)

eobj=E()
eobj.c1()
eobj.c2()
eobj.c3()


#hairarchy inheritance
print("this is hairarchy inheritance")
class C:
    x,y=100,200
    def c1(self):
        print(self.x+self.y)

class D(C):
    a,b=300,400
    def c2(self):
        print(self.a-self.b)

class E(C):
    i,j=2,5
    def c3(self):
        print(self.i*self.j)

dobj= D()
dobj.c1()
dobj.c2()
eobj=E()
eobj.c1()
eobj.c3()


#Multiple inheritance

print("this is multiple inheritance")

class C:
    x,y=100,200
    def c1(self):
        print(self.x+self.y)

class D:
    a,b=300,400
    def c2(self):
        print(self.a-self.b)

class E(C,D):
    i,j=2,5
    def c3(self):
        print(self.i*self.j)

eobj=E()
eobj.c1()
eobj.c2()
eobj.c3()

#overridding 
print("this is method overriding")
class A:
    def m1(self):
        print("this is m1 from A class")

class B(A):
    def m1(self,a,b):
        print("this is m1 from B class")
        super().m1()                        #accsss parent class method
bobj=B()
bobj.m1(100,200)

#overloading polymorphism

class Human:
    def sayhello(self,name=None):
        if name is not None:
            print("hello "+name)
        else:
            print("Hello")

h=Human()
h.sayhello("scott")
h.sayhello()

#overloading example2
class Caculator:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)

c=Caculator()
c.add()
c.add(10,20)
c.add(10,20,30)