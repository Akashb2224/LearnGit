print("this is multiple inheritance")

class C:
    x,y=100,200
    def c1(self):
        print(self.x+self.y)

class D:
    a,b=300,400
    def c1(self):
        print(self.a-self.b)

class E(C,D):
    i,j=2,5
    def c3(self):
        print(self.i*self.j)

eobj=E()
eobj.c1()
# eobj.c2()
# eobj.c3()