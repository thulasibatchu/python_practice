class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_info(self):
        print("Name:",self.name,"age:",self.age)

a=Person("Thulasi",23)
a.show_info()

