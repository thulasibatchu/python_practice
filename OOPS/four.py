# class Employee:
#     def __init__(self):
#         pass
#     def setname(self):
#         pass
#     @classmethod
#     def setorg_name(cls):
#         pass
#     @staticmethod
#     def calc():
#         pass

class Account:
    def __init__(self,id,name):
        self.eid=id
        self.ename=name
    def setsalary(self,sal):
        self.esal=sal

a1=Account(101,'rahul')
a2=Account(102,'sonia')
a1.setsalary(45000)
a2.setsalary(55000)
a1.eloc="wayanad"
print(a1.__dict__)
print(a2.__dict__)
