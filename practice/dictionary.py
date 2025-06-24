a="cat rat cat rat cat"
b={'cat':0,'rat':0}
c=a.split()
for i in c:
   if i=='cat':
        b['cat'] +=1
   else:
        b['rat'] +=1
for key,value in b.items():
    print(key,":",value)


