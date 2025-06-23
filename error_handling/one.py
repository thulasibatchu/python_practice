# print(10/5)
# print(10/0)
# print(10/1)
# print("good afternoon")


print(10/5)
try:
    print(10/0)
except ZeroDivisionError as err:
    print(10/1)

print("good afternoon")