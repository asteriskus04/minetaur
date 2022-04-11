import psycopg2
from psycopg2 import OperationalError

connection = psycopg2.connect(
    user="minetaur",
    password="qwerty123",
    host="abormotov.ru",
    port="5433",
    database=""
)


def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(query)
    print("Query executed successfully")


delete_users = "DELETE FROM IP"
execute_query(connection, delete_users)

create_users_table = """
CREATE TABLE IF NOT EXISTS IP (
id SERIAL PRIMARY KEY,
  ip1 TEXT,
  ip2 TEXT, 
  port1 INTEGER,
  port2 INTEGER,
  time1 TEXT,
  time2 TEXT,
  chislo INTEGER,
  HEX TEXT
)
"""
execute_query(connection, create_users_table)

IPs = [
    ("192.168.1.2", "192.168.1.3", 4322, 80, "0.6777", "0.7728", 1,
     "005600730065006d002000700072006900760065007400200074006500730074"),
    ("192.168.1.3", "192.168.1.4", 4322, 80, "0.6777", "0.7729", 1,
     "005600730065006d0020007000720069007600650074010827598612598681")
]

user_records = ", ".join(["%s"] * len(IPs))

insert_query = (
    f"INSERT INTO IP (ip1, ip2, port1, port2, time1, time2, chislo, HEX) VALUES {user_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, IPs)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def hex_to_utf(a):
    for i in range(len(a)):
        b = bytes.fromhex(a[i])
        a = b.decode('utf-8')
        return a


select_hex = "SELECT HEX FROM IP"
hex = execute_read_query(connection, select_hex)
print(hex)
print(hex_to_utf(hex))

# print(hex_to_utf(hex1))
m = "005600730065006d002000700072006900760065007400200074006500730074"
# print(hex_to_utf(m))
