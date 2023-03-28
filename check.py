import psycopg2
from psycopg2 import Error

try:
    connection = psycopg2.connect(user="hubuser_87456",
                                  password="bQiX58C3^aFreNDH",
                                  host="46.235.227.121",
                                  port="38476",
                                  database="hub_87456")

    cursor = connection.cursor()
    # # SQL query to create a new table
    # create_table_query = '''CREATE TABLE mobile
    #       (ID INT PRIMARY KEY     NOT NULL,
    #       MODEL           TEXT    NOT NULL,
    #       PRICE         REAL); '''
    # # Execute a command: this creates a new table
    # cursor.execute(create_table_query)
    # connection.commit()
    print("Table created successfully in PostgreSQL ")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")