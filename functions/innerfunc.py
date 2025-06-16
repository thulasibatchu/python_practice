# def outer():
#     print("outer started")
    
#     def inner():
#         print("inner started")
#     inner()
    
#     def login():
#         print("login success")
#     login()

# outer()

def outer():
    print("outer started")
    
    def inner():
        print("inner started")
        
    
    def login():
        print("login success")
    return inner

inner=outer()
inner()
