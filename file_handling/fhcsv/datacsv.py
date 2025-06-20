import csv
fp=open('emp.csv','r')
emp_csv_obj=csv.reader(fp)
for emp_list in list(emp_csv_obj)[1:]:
     print(emp_list[1])