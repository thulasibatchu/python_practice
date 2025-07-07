import requests,mysql.connector
users=None
dbcon=None
user_table_data=[]
try:
    user_data=requests.get("https://jsonplaceholder.typicode.com/users")
    users=user_data.json()
    for user in users:
        user_table_data.append((user['id'],user['username'],user['email']))
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='dbone')
    cursor=dbcon.cursor()
    sql_st= ''' 
              INSERT INTO users
              values
              (%s,%s,%s);
            '''
    cursor.executemany(sql_st,user_table_data)
    dbcon.commit()
    print('data inserted')
except mysql.connector.errors.Error as Error:
    print(Error.msg)