class Person:
    def __init__(self,name,marks=60,age=18):
        self.name=name
        self.age=age
        self.marks=marks
    def show_info(self):
        print("Name:",self.name,"age:",self.age,"marks:",self.marks)
    
    def __str__(self):
        return f"name:{self.name},age:{self.age},marks:{self.marks}"
    
    def grade(self):
        if self.marks>90:
            return 'A'
        elif self.marks>=75:
            return 'B'
        else:
            return 'C'

a=Person("Thulasi",87,23)

# a.age=24
# a.show_info()
# print(a.grade())
# b=Person("rg")
# b.show_info()
# print(b.grade())
# print(a.age)

print(a)
print(b)
