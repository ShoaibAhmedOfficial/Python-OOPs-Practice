class DemoClass:
    a = 10
    b=25
    def __init__(self):
        print("welcome to the HomeLand")
    def showvalue(self):
        print(self.a)

    def showvalues(self):
        self.c =self.b*self.b
        print(self.c)

    def showvalue1(self):
        print("Welcome to the page")

    def showvalue2(self,a,b):
        print(a+b*b)

obj=DemoClass()
obj.showvalue()
obj.showvalues()
obj.showvalue1()
obj.showvalue2(20,30)