import mysql.connector
dbcon=None
cursor=None
try:
    dbcon=mysql.connector.connect(host='localhost',user='root',password='root',database='dbone')
    cursor=dbcon.cursor()
    sql_st='''
                INSERT INTO Employees
                values
                (101,'rahul',45000.45);
            '''
    
    cursor.execute(sql_st)
    dbcon.commit()
    print("New employee data recorded successfully!")
except mysql.connector.errors.Error as error:
    print(error)
