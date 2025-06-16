# def smart_div(func):
#     def inner(a,b):
#         if b==0:
#             print('cannot divide by zero')
#         else:
#             return func(a,b)
#     return inner 


# @smart_div
# def calc(a,b):
#     print(a/b)

# calc(10,2)
# calc(10,0)
# print("GM")


def login_req(func):
    def inner(name,status):
        if status==False:
            print('login is req')
        else:
            return func(name,status)
    return inner


def home_page(name,status):
    print('homepage')
@login_req
def order_page(name,status):
    print('order_page')
@login_req    
def update_profile(name,status):
    print('update_profile')

def contact_page(name,status):
    print('contact_page')


# home_page('rg',False)
# order_page('rg',False)
# update_profile('rg',False)
# contact_page('rg',True)


