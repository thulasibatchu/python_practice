a=[5,7,1,2,3,5,1,2]
# a.append(5)
# print(a)

# a.remove(3)
# print(a)
# a.sort()
# print(a)

# a.reverse()
# print(a)

# sum=0
# for i in a:
#    sum=sum+i
# print(sum)
# avg=sum/len(a)
# print(avg)

b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
print(b)



