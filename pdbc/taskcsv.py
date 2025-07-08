import requests,csv
try:
    data=requests.get('https://jsonplaceholder.typicode.com/users')
    user_data=data.json()
    users=user_data

    new_users=[]
    for user in users:
        new_users.append([user['id'],user['name'],user['email']])
    
    fp=open('users.csv','w',newline='')
    csvwriter=csv.writer(fp)
    csvwriter.writerow(['id','name','email'])
    csvwriter.writerows(new_users)

except Exception as e:
   print("error occured",e)

finally:
    fp.close()
