import mysql.connector
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='dbone')
    cursor=dbcon.cursor()
    sql_st='''
                CREATE TABLE  employees(
                eid int, 
                ename varchar(32),
                esal float
                );
            '''
    cursor.execute(sql_st)
    print("New Table created successfully!")
except mysql.connector.errors.Error as error:
    print(error)
