import pymysql

try:

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



#//////////////////////////////////////////////////////////
# registration of user

tel = str(input("enter tel --->  "))
name = str(input("enter name --->  "))
lastname = str(input("enter lastname --->  "))
l_lastname = str(input("enter l_lastname --->  "))


def registration(tel,name,lastname,l_lastname):
    try:
        mycursor = connection.cursor()
        sql = "INSERT INTO reg_user (tel, name, lastname,l_lastname) VALUES (%s, %s, %s, %s)"
        val = (tel,name,lastname,l_lastname)  
        mycursor.execute(sql, val)
        connection.commit()
        print(mycursor.rowcount, "Дані внесено")

        reg = """
    
SELECT name,lastname,l_lastname FROM reg_user 
EXCEPT
SELECT name,lastname,l_lastname FROM valid_user

    """ 
        reg_matched = """
SELECT name, COUNT(name)
FROM reg_user
GROUP BY name
HAVING COUNT(name) > 1

        """
 
        print(mycursor.execute(reg))
        print(mycursor.execute(reg_matched))

        if( mycursor.execute(reg) > 0):
            sql ="""delete from reg_user
                    order by user_id desc limit 1"""
            # val = (tel,name,lastname,l_lastname)
            mycursor.execute(sql)
            connection.commit()
            print(mycursor.rowcount, " Дані Видалено ")
            print(" Registration error ")
        elif(mycursor.execute(reg_matched)== 1):
            sql ="""delete from reg_user
                    order by user_id desc limit 1"""
            # val = (tel,name,lastname,l_lastname)
            mycursor.execute(sql)
            connection.commit()
            print(mycursor.rowcount, " Дані Видалено ")
            print(" Registration error ")
        elif(mycursor.execute(reg) == 0):
            print(" You registred ")


        
        
    except Exception as e:
        print("troubles with mySQL code !!!!")
            
registration(tel,name,lastname,l_lastname)

#///////////////////////////////////////////////