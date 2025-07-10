class Student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    
    def show_info(self):
        print("name:",self.name,"roll_number:",self.roll_number,"marks:",self.marks)

    def total_marks(self):
        total=0
        for mark in self.marks:
            total=total+mark
        return total
    
    def average_marks(self):
        avgs=self.total_marks()/len(self.marks)
        return avgs
    
    def result(self):
        if self.average_marks()>=40:
            return 'pass'
        else:
            return 'fail'
    
s1= Student("Thulasi", "22A91", [70, 80, 90, 60, 75])
s1.show_info()
print(s1.total_marks())
print(s1.average_marks())
print(s1.result())
