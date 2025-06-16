# def addone(price):
#     return price+1
    
# product_prices=[98,198,298,398,498]    
# map_obj=map(addone,product_prices)
# new_prices=list(map_obj)
# print(new_prices)


# print(list(map(lambda price:price+1,[98,198,298,398,498])))

# enames=['rahul','sonia','priya']
# # def changecase(enames):
# #     return enames.upper()
# # new_names=list(map(changecase,enames))
# # print(new_names)
# print(list(map(lambda enames:enames.upper(),enames)))

numbers=[37,18,31,14,8,12,7]
# even_numbers=[]
# for num in numbers:
#         if num%2==0:
#            even_numbers.append(num)
# print(even_numbers) 

# def check_even(numbers):
#      return numbers%2==0

# even_numbers=list(filter(check_even,numbers))
# print(even_numbers)

print(list(filter(lambda num:num%2==0,numbers)))  



