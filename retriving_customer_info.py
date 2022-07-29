import mysql.connector
from customer_db_connect_fun import *
try:
    con=customer_db_details()
    cursor=con.cursor()
    query_string=("select * from tbl_customer1_info")
    cursor.execute(query_string)
    data=cursor.fetchall()
    print("data of tbl_customer_info: ",data)
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("problem with sql",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
