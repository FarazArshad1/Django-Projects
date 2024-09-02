import mysql.connector

def database_Connect():
     mydb = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "Lhrfscmm1712553",
                database = 'school_erp'
            )
     return mydb