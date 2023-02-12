import sqlite3
try:
    con = sqlite3.connect('main.db')
    cursor = con.cursor()
    print("Successfully Connected to SQLite")
    name = "Ivan"
    data_insert = """
    INSERT INTO validUser
                          (name) 
                           VALUES 
                          ("Ivan")
    
    """
    cursor.execute(data_insert)
    con.commit()
except sqlite3.Error as error:
    print("Failed to insert data into sqlite table", error)