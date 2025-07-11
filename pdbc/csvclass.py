import requests
import csv
import json
import mysql.connector
import pymongo

#Extract Data
users_resp=requests.get('https://jsonplaceholder.typicode.com/users')
users=users_resp.json()
print(type(users))

#Transform - csv file and mysql table - ie users
#Tranform  - json file and mongoDB
users_data =[]
user_json_data=[]
for user in users:
    user_json_data.append({'uid':user['id'],'uname':user['username'],
                           "email":user['email'],
                           "city":user['address']['city']}) 
    
    users_data.append((user['id'],user['username'],
                       user['email'],
                       user['address']['city']))






#print(user_json_data)
#Load data into users.csv file

fp1=open("users2.csv",'w',newline='')
cw_obj=csv.writer(fp1)
cw_obj.writerow(['uid','uname','email','city'])
cw_obj.writerows(users_data) #List of tuple values
print("New CSV File Created!")

fp2=open("users.json",'w')
json.dump(user_json_data,fp2)
print("New JSON File created")


dbcon=None
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='dbone')
    cursor=dbcon.cursor()
    sql_st="""
            insert into users
            values
            (%s,%s,%s,%s);
           """
    cursor.executemany(sql_st,users_data)
    dbcon.commit()
    print("Data Inserted Successfully")
except mysql.connector.errors.Error as err:
    print(err)

#Load into MongoDB
dbclient=None 
try:
    dbclient=pymongo.MongoClient()
    db=dbclient['dbtwo']
    users_col=db['users']
    users_col.insert_many(user_json_data)
    print("Data inserted into collection")
except:
    pass