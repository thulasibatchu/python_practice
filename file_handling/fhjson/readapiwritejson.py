import requests,json
api_url='https://jsonplaceholder.typicode.com/users'

response_data=requests.get(api_url)
users=response_data.json()
print(type(users))

fp=open('new_users.json','w')
json.dump(users,fp)

print('new file created')

fp.close()
