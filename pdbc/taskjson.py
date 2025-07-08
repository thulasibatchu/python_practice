import requests,json
try:
    data=requests.get('https://dummyjson.com/users')

    users=data.json()
    fp=open('new_user.json','w')
    json.dump(users,fp)

    print('new file created')


except Exception as e:
   print("error occured",e)

finally:
  fp.close()