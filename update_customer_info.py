import mysql.connector
from customer_db_connect_fun import *
try:
    con=customer_db_details()
    cursor=con.cursor()
    query_string=("update tbl_customer1_info SET Last_Name='Yadagiri' where First_Name='Padma';")
    cursor.execute(query_string)
    con.commit()
except mysql.connector.DatabaseError as e:
    if con:
        con.rollback()
        print("problem with sql:",e)
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()
