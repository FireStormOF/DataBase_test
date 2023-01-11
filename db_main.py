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
        val_1 =(name,lastname) 
        
        valid = 'SELECT name,lastname \t FROM \t ( \t SELECT valid_user.name, valid_user.lastname \t FROM valid_user \t UNION ALL \t SELECT reg_user.name, reg_user.lastname  \t FROM reg_user) t \t GROUP BY name, lastname \t HAVING COUNT(*) = 1  \t ORDER BY name'


        invalid = 'SELECT name,lastname \t FROM \t ( \t SELECT valid_user.name, valid_user.lastname \t FROM valid_user \t UNION ALL \t SELECT reg_user.name, reg_user.lastname  \t FROM reg_user) t \t GROUP BY name, lastname \t HAVING COUNT(*) > 1  \t ORDER BY name'
         

        # mycursor.execute(invalid,val_1)
        # mycursor.execute(valid,val_1)
        
        if( mycursor.execute(invalid,val_1)):
            print("Ви вже зареєстровані в системі, не треба нас дурити <3 ")
        elif(  mycursor.execute(valid,val_1)):
            mycursor = connection.cursor()
            sql = "INSERT INTO reg_user (name, lastname) VALUES (%s, %s)"
            val = (name,lastname)
            mycursor.execute(sql, val)
            connection.commit()
            print(mycursor.rowcount, "Дані внесено")
        
    except Exception as e:
        print("Я даун")
            





registration(name,lastname)




# validation of user


# add to main