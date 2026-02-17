class Student:
    __name="Shoaib"
    def __init__(self):
        print(self.__name)
        self.__displayinfo()
    def __displayinfo(self):
        print("Welcome to Home")

obj=Student()
# print(obj.__name)