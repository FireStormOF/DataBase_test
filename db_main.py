import pymysql

def bd_connect(host,user,password,database):
    try:
        # connect to exist database
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database   
        )
        connection.autocommit = True
        
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT version();"
            )
            
            print(f"Server version: {cursor.fetchone()}")
            
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")

# bd_connect("localhost","root","123Qwerty123","Test_bd")