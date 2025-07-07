class Test:
    min_bal=500  #static variable
    def __init__(self,id,name):
        print("constructor method")
    def m1(self):
        self.acc_bal=200  #instance variable
        pass
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        tax=5   #local variable
        pass

t1=Test()
