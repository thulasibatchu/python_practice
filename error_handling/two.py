# fp=open('xyz.txt','r')
# data=fp.read()
# print(data)
# print("gm")
# fp.close()

fp=None
try:
   fp=open('xyz.txt','r') 
except:
   fp=open('default.txt','r')
data=fp.read()
print(data)
print("Good Morning")
fp.close()

