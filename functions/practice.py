# n=5
# for i in range(1,11):
#     print(i*n,end=" ")

# n='cat rat cat rat cat'
# cat_count = n.split().count('cat')
# rat_count = n.split().count('rat')
# if cat_count==rat_count:
#     print(True)
# else:
#     print(False)







# sentence = "apple banana apple orange banana apple"
# sentence_break=sentence.split()
# sentence_count={}
# for breaks in sentence_break:
#     if breaks in sentence_count:
#         sentence_count[breaks]+=1
#     else:
#         sentence_count[breaks]=1

# for breaks,count in sentence_count.items():
#    print(breaks,":",count)



# sentence = "red blue red green blue red"
# highest_count={}
# words=sentence.split()
# for word in words:
#     if word in highest_count:
#         highest_count[word]+=1
#     else:
#         highest_count[word]=1

# for word,count in highest_count.items():
#     print(word,":",count)

# print(max(highest_count.items()))


# name=input("Enter name:")
# age=input("Enter age:")

# print("hello",name ,"you are",age,"years old")

# num=int(input("enter a number:"))
# if num%2==0:
#     print("even number")
# else:
#     print("odd number")

# num=int(input("enter a number:"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("num is zero")

# marks=int(input("enter a number:"))
# if marks>90:
#     print("A")
# elif marks>75 and marks<90:
#     print("B")
# elif marks>50 and marks<75:
#     print("C")
# else:
#     print("Fail")

a=10
b=2
c=24
if a>b and a>c:
    print(a)
elif b>c and b>a:
    print(b)
else:
    print(c)



    