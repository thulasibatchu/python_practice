# a="thulasi"
# vowels="aeiou"
# count=0
# for i in a:
#     if i in vowels:
#       count+=1
# print(count)

# for i in vowels:
#     if i in a:
#         a=a.replace(i,"")
# print(a)

# a="madam"
# b=""
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]

# print(b)
# if a==b:
#     print("is a palindrome")
# else:
#     print("not a palindrome")

# a="apple"
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# for i,count in freq.items():
#     print(i,":",count)

# a="hello world this is string"
# # a=a.replace(" ","-")
# # print(a)

# b=a.split()
# for i in range(len(b)):
#     b[i]=b[i].capitalize()
# result=' '.join(b)
# print(result)

a="bananas"
# b=""
# for i in a:
#     if i not in b:
#         b+=i
# print(b)

b={}
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

# max_count=max(b.items(),key=lambda item:item[1])
# print(max_count[0],max_count[1])

for i,count in b.items():
    if count==1:
        print(i,count)












