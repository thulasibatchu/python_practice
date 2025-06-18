import json
fp1=open('emp.json','r')
fp2=open('users.json','w')

users=json.load(fp1)
json.dump(users,fp2)
print("newfile created")
fp1.close()
fp2.close()