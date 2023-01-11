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

# tel = str(input("enter tel...  "))
name = str(input("enter name...  "))
lastname = str(input("enter lastname...  "))
# l_lastname = str(input("enter l_lastname...  "))

def registration(name,lastname):
    try:
        mycursor = connection.cursor()

        mycursor = connection.cursor()
        sql = "INSERT INTO reg_user (name, lastname) VALUES (%s, %s)"
        val = (name,lastname)  
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.rowcount, "Дані внесено")

        invalid = """ select name, lastname
       from (
         select name, lastname
         from reg_user
         union all
         select name, lastname
         from valid_user)
       temp
       group by name, lastname 
       having count(*) = 1; """

        valid = """ select name, lastname
       from (
         select name, lastname
         from reg_user
         union all
         select name, lastname
         from valid_user)
       temp
       group by name, lastname 
       having count(*) = 0; """






        print( mycursor.execute(invalid) )
        print("---------------")
        print( mycursor.execute(valid) )

        if( mycursor.execute(invalid) > 1 ):
            sql = "INSERT INTO reg_user (name, lastname) VALUES (%s, %s)"
            val = (name,lastname)  
            mycursor.execute(sql, val)
            connection.commit()
            print(mycursor.rowcount, "Дані Видалено")
        elif( mycursor.execute(valid) == 1 ):
            print(" You registred )))) ")
        
    except Exception as e:
        print("Я стаю менш дауном")
            





registration(name,lastname)




# validation of user


# add to main