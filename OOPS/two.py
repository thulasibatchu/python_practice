# class Account:
#     def open_account(self):
#         print("Account opened") 
#     def deposit_money(self):
#         print("amount deposited")
#     def withdrawl(self):
#         print("amount Withdrawn")

# a1=Account()
# a1.open_account()
# a1.deposit_money()
# a1.withdrawl()

# print("******")

# a2=Account()
# a2.open_account()
# a2.deposit_money()
# a2.withdrawl()

class Account:
    def open_account(self):
        print("Account opened") 
    def deposit_money(self,amount):
        print(amount,"amount deposited")

a1=Account()
a2=Account()

a1.open_account()
a1.deposit_money(50000)