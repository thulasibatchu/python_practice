class Parent:
    def m1(self):
        print("Parent class - m1 method") 
    def m2(self):
        print("Parent class - m2 method") 

class Child(Parent):
    def m3(self):
        print("Child class - m3 method")  

c1=Child()
print(c1.__dict__)
c1.m1()
c1.m2()
c1.m3()