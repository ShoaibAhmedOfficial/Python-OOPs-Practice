class A:
    def showData(self):
        print("I'm in A")
class B(A):
    def showData(self):
        print("i'm in B")

obj=B()
obj.showData()