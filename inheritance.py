class A:
    def displayA(self):
        print("welcome to the party")

class B(A):
    def displayB(self):
        print("welcome to the our party")

class C(B):
    def displayC(self):
        print("Welcome to the party bhai")

obj=C()
obj.displayA()
obj.displayB()
obj.displayC()