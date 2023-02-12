import sqlite3
try:
    con = sqlite3.connect('D:\Proj_main\main.db')
    cursor = con.cursor()
    print("Successfully Connected to SQLite")
    # name = "MAX"
    # data_insert = f"""
    # INSERT INTO validUser
    #                       (name) 
    #                        VALUES 
    #                       ("{name}")
    
    # """
    Telegram_id = 234235235
    name = "name"
    lastname = "lname"
    patronymic = "pat"
    course = "1"
    spec = "cs-15"
    band = "gr"
    sql = f"""INSERT INTO validUser(Telegram_id, name, lastname, patronymic, course, spec) \
                                            VALUES("{Telegram_id}", "{name}", "{lastname}", "{patronymic}", "{course}", "{spec}")"""
    cursor.execute(sql)
    con.commit()

except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)