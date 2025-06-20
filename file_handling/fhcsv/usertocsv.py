import requests,csv

data=requests.get('https://dummyjson.com/users')
user_data=data.json()
users=user_data['users']
print(len(users))

new_users=[]
for user in users:
    new_users.append([user['id'],user['firstName'],user['age']])

fp=open('users.csv','w',newline='')
csvwriter=csv.writer(fp)
csvwriter.writerow(['uid','uname','age'])
csvwriter.writerows(new_users)