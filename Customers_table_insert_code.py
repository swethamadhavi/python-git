import mysql.connector
from customer_db_connect_fun import *
try:
    con=customer_db_details()
    cursor=con.cursor()
    create_query_string=("Create Table tbl_customer1_info(Customer_ID int primary key,First_Name varchar(100),Last_Name varchar(100),Mobile_Number decimal(15,0),Address varchar(200),pincode int);")
    cursor.execute(create_query_string)
    query_string="insert into tbl_customer1_info(Customer_ID,First_Name,Last_Name,Mobile_Number,Address,pincode) values(%s,%s,%s,%s,%s,%s)"
    values=[('2344','Swetha','Madhavi','1234567891','Vijayawada','529918'),('4556','lucky','Yadagiri','2345678912','Hyderabad','345675'),('2345','Lalu','test','5677789899','Chennai','456789'),('2346','Padma','example','3456721897','Bengaluru','345679')]
    cursor.executemany(query_string,values)
    con.commit()
    print("Inserted Successfully")
except Exception as e:
    if con:
        con.rollback()
        print("problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
