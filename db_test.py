import sqlite3
try:
    con = sqlite3.connect('D:\Proj_main\main.db')
    cursor = con.cursor()
    print("Successfully Connected to SQLite")

    id_select = """
    select Telegram_id from validUser
    """
    cursor.execute(id_select)
    con.commit()
    list  = cursor.fetchall()
    print(list)
except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)