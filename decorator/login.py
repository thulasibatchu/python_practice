from intro import login_req

def home_page(name,status):
    print('home page')

@login_req
def order_page(name,status):
    print('order_details') 
@login_req 
def update_profile(name,status):
    print('updating_profile')
def contact_page(name,status):
    print('contact us page')

home_page('rg',False)
order_page('rg',False)
update_profile('rg',False)
contact_page('rg',True)
