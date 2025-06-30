# s="hello world"
# print(s.count('a'))

# s1=s.reverse()
# if s1==s:
#     print("s is palindrome")

# print(s.split())
# for word in s.split():
#     print(word)

# s="madams"
# if s==s[::-1]:
#     print('s is palindrome')
# else:
#     print('s is not a palindrome')

# vowels='aeiou'
# for i in vowels:
#     s=s.replace(i,'*')
# print(s)

# words="this is a word i thought but"
# a=words.split()
# print(len(a))

# s='silent'
# a='listen'

# if sorted(s)==sorted(a):
#     print("yes it is a anagram")
# else:
#     print("not an anagram")

# text='banana'
# freq={}
# for ch in text:
#     if ch not in freq:
#         freq[ch]=text.count(ch)
# for ch,count in freq.items():
#     print(ch,":",freq)

# input= "apple banana apple orange apple"
# freq={}
# fruits=input.split()
# print(fruits)
# for fruit in fruits:
#     if fruit in freq:
#         freq[fruit]=fruits.count(fruit)
# for fruit,count in freq.items():
#     print(fruit,freq)


# a="Hello world"
# vowels='aeiou'
# count=0
# for i in vowels:
#     count+=a.count(i)
# print(count)

# for i in vowels:
#     a=a.replace(i,'')
# print(a)

# a="python"
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev+=a[i]

# print(rev)

# i='aabc'
# j='abbc'
# if len(i)!=len(j):
#     print(False)
# else:
#     match=True
#     for ch in i:
#        if i.count(ch)!=j.count(ch):
#            match=False
#            break
#     print(match)

# a="hello world python"
# b=a.replace(" ","-")
# print(b)

# a="hello world"
# b=a.split()
# print(b)
# for i in range(len(b)):
#     b[i]=b[i].capitalize()
# result=' '.join(b)
# print(result)

# a="Hello World"
# vowels="aeiou"
# for i in vowels:
#     a=a.replace(i,'')
# print(a)

# a="thulasi"
# b=''
# for i in range(len(a)-1,-1,-1):
#     b+=a[i]
    
# print(b)

# a="aabc"
# b="abac"
# if len(a)!=len(b):
#     print(False)
# else:
#     for ch in a:
#       match=True
#       if a.count(ch)!=b.count(ch):
#          match=False
#          break
#     print(match)

#using dict
# freq_a={}
# freq_b={}
# for i in a:
#     if i in freq_a:
#         freq_a[i]+=1
#     else:
#         freq_a[i]=1
# for j in b:
#     if j in freq_b:
#         freq_b[j]+=1
#     else:
#         freq_a[j]=1

# if freq_a==freq_b:
#     print(True)
# else:
#     print(False)

# a="malayalam"
# b={}
# for i in a:
#     if i in b:
#         b[i]+=1
#     else:
#         b[i]=1
# for i,count in b.items():
#     print(i,":",count)

# max_char=max(b.items(),key=lambda item: item[1])  
# #lambda function says take value to count highest frequency
# #item is value of key so it's index is 1 as key is 0
# print("highest frequency character",max_char[0])
# print("count of highest frequency character",max_char[1])

sentence = "apple banana apple orange banana apple"
a=sentence.split()
b={}
print(a)
for i in a:
    if i in b:
        b[i]+=1
    else:
        b[i]=1

for i,count in b.items():
    print(i,count)

# max_count=max(b.items(),key=lambda item:item[1])
# print(max_count[0],max_count[1])

min_count=min(b.items(),key=lambda item:item[1])
print(min_count[0],min_count[1])



















