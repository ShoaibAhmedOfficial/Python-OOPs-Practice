# l=[10,20,30]
# print(len(l))
# s="Welcome to School"
# print(len(s))

class Ws:
    def displayinfo(self):
        print("Welcome to Wscubetech")
class IIP(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("Welcome to IIP")

obj=IIP()
obj.displayinfo()