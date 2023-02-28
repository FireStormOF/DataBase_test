import sqlite3
try:
    con = sqlite3.connect('D:\Proj_main\main.db')
    cursor = con.cursor()
    print("Successfully Connected to SQLite")
except sqlite3.Error as error:
    print("Failed to connect to SQLite", error)


# try: 
#     Telegram_id = 12345678
#     name = "Іван"
#     lastname = "Ящук"
#     patronymic = "Володимирович"
#     check =f"""
#     UPDATE
# 	validUser
# SET
# 	Telegram_id = '{Telegram_id}'
# WHERE
# 	name LIKE "{name}" and 
# 	lastname LIKE "{lastname}"and
# 	patronymic LIKE "{patronymic}";
#     """
#     cursor.execute(check)
#     con.commit()
#     print("OK")
    
# except Exception as e:
#     print("FUCK")    

try:
    faculty ="фіс"
   

#     for_all ="""
# SELECT
# 	Telegram_id
# FROM
# 	validUser
#     """
    for_faculty = f"""
SELECT Telegram_id
FROM validUser
WHERE band = "{faculty}"
    """    
    cursor.execute(for_faculty)
    print(cursor.fetchall())
    con.commit()

except Exception as e:
    print("There was an error:", e)  

try: 
    spec = "123"
    for_spec = f"""
SELECT
	Telegram_id
FROM
	validUser
WHERE
	spec = "{spec}"
    """    
    cursor.execute(for_spec)
    print(cursor.fetchall())
    con.commit()  
except Exception as e:
     print("There was an error:", e)     
  