s="hello world"
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

text='banana'
freq={}
for ch in text:
    if ch not in freq:
        freq[ch]=text.count(ch)
for ch,count in freq.items():
    print(ch,":",freq)












