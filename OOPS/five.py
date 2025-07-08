# class Account:
#     def __init__(self,id,name,amount):
#         self.acc_id=id 
#         self.acc_name=name 
#         self.acc_bal=amount

#     def deposit_amount(self,amount):
#         self.acc_bal=self.acc_bal+amount

# a1=Account(101,'Rahul',5000)
# a1.deposit_amount(100)
# a1.deposit_amount(200)

# a2=Account(102,'Sonia',15000)
# a2.deposit_amount(2500)
# print(a1.__dict__)
# print(a2.__dict__)

class Employee:
    company_name='TCS'    #static variable-one copy

    def __init__(self,id,name,sal):
        self.eid=id
        self.ename=name 
        self.esal = sal 
e1=Employee(101,'Rahul',45000)
e2=Employee(102,'Sonia',55000)
e3=Employee(103,'Priya',65000)

print(Employee.__dict__)
print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)