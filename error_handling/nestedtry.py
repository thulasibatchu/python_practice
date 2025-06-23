fp=None
num=None
try:
    a=int(input("Enter a:"))
    b=int(input("Enter b:"))
    print(a/b)
    fp=open('xyz.txt','r')
except ValueError as err:
    print("pls enter digits")
except ZeroDivisionError as err:
    print("cannot divide by zero")
except FileNotFoundError as err:
    print("file not found please check")
except:
    print("pls check")


