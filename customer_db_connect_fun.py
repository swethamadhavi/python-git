import mysql.connector
def customer_db_details():
    con=mysql.connector.connect(user='root',password='Swetha@123',host='localhost',database='department',port=3306)
    return con