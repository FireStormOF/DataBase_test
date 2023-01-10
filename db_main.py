import pymysql

# def bd_connect(host,user,password,database):
try:
        # connect to exist database
        connection = pymysql.connect(
            host='localhost',
            user="root",
            password="123Qwerty123",
            database='Test_bd'   
        )
        connection.autocommit = True
        
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            
            print(f"Server version: {cursor.fetchone()}")
            
except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
# finally:
#         if connection:
#             # cursor.close()
#             connection.close()
#             print("[INFO] PostgreSQL connection closed")

# bd_connect("localhost","root","123Qwerty123","Test_bd")  

# registration of user

tel = str(input("enter tel...  "))
name = str(input("enter name...  "))
lastname = str(input("enter lastname...  "))
l_lastname = str(input("enter l_lastname...  "))

def registration(tel,name,lastname,l_lastname):
    try:
        mycursor = connection.cursor()
        sql = "INSERT INTO reg_user (tel, name, lastname, l_lastname) VALUES (%s, %s, %s, %s)"
        val = (tel, name,lastname, l_lastname)
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.rowcount, "Дані внесено")
    except:
        pass    





registration(tel,name,lastname,l_lastname)




# validation of user


# add to main