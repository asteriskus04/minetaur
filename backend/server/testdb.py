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

delete_users = "DELETE FROM users"
execute_query(connection, delete_users)

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL, 
  age INTEGER,
  gender TEXT,
  nationality TEXT
)
"""
execute_query(connection, create_users_table)

users = [
    ("Лера", 20, "Ж", "Россия"),
    ("Сухив", 20, "М", "Россия"),
    ("Тор", 41, "М", "Украина"),
    ("Юра", 120, "М", "Молдавия"),
]

user_records = ", ".join(["%s"] * len(users))

insert_query = (
    f"INSERT INTO users (name, age, gender, nationality) VALUES {user_records}"
)

connection.autocommit = True
cursor = connection.cursor()
cursor.execute(insert_query, users)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")

select_users = "SELECT name, age, gender, nationality FROM users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)
