# a=("python","java","c++")
# print("first language:",a[0])
# print("last language:",a[-1])
# print(len(a))


# def sum_avg(nums):
#    sums=0
#    for i in range(len(nums)):
#     sums=sums+nums[i]

#    avgs=sums/len(nums)
#    return (sums,avgs)
 
# nums=[10,20,30]
# result=sum_avg(nums)
# print(result[0])
# print(result[1])

# students=[("thulasi",90),("ravi",80),("pooja",75)]
# for name,score in students:
#     print(name,"scored",score)

a={
    (0,0):"Home",
    (5,6):"office",
    (2,3):"market"
}

for location,items in a.items():
    print("at location",location,":",items)

print(a[(2,3)])