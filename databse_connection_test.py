import psycopg2
import psycopg2.pool
import random
import string
import time

# Connection Pool
connection_pool = psycopg2.pool.SimpleConnectionPool(
    10,  # minconn
    20,  # maxconn
    host='212.71.253.204',
    port='38476',
    user='hubuser_2111191',
    password='5gjdu9sywhhrpmcdmzfdvm8sjp34dbb0',
    database='hub_2111191'
)

def check_server_connection(connection):
    try:
        connection.cursor().execute("SELECT 1")
        return True
    except psycopg2.OperationalError:
        return False

def generate_random_clientcode():
    """Generate a random clientcode."""
    prefix = "zeuz update "
    suffix = random.randint(1, 10000)
    return prefix + str(suffix)

def update_data_in_table(connection, table_name , total_time_difference):
    with connection.cursor() as cursor:
        query_select = f"SELECT id, clientcode FROM {table_name};"
        cursor.execute(query_select)
        rows = cursor.fetchall()
        count_down = 0
        for row in rows:
            new_clientcode = generate_random_clientcode()
            update_query = f"UPDATE {table_name} SET clientcode = %s WHERE id = %s;"
            cursor.execute(update_query, (new_clientcode, row[0]))
            print(f"Row with id {row[0]} updated with clientcode: {new_clientcode}")
            connection.commit()
            if total_time_difference == count_down:
                break
            count_down += 1
            print(count_down)
        return "time complete"


# Run the update for 5 minutes
start_time = time.time()

end_time = start_time + 10
total_time_difference = end_time - start_time
count_down = 0
with connection_pool.getconn() as conn:
    if check_server_connection(conn):
        print("Server connection is OK")

        while (True):
            end_result = update_data_in_table(conn, 'client', total_time_difference)
            if end_result == "time complete":
                break
    else:
        print("Server connection failed")

connection_pool.closeall()
