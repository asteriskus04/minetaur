import psycopg2
import sys

connection = psycopg2.connect(
    user="minetaur",
    password="qwerty123",
    host="abormotov.ru",
    port="5433",
    database="minetaur"
)

cursor = connection.cursor()
print("Информация о сервере PostgreSQL")
print(connection.get_dsn_parameters(), "\n")
cursor.execute("SELECT version();")
record = cursor.fetchone()
print("Вы подключены к - ", record, "\n")
print()
# делаем запрос к БД и выводим наименование всех БД
cursor.execute("SELECT * FROM pg_catalog.pg_tables")
# запишем в массив результат поиска
rows = cursor.fetchall()
# сортируем по алфавиту список с наименованиями БД
rows.sort()
# выводим в консоль наименование БД
for row in rows:
    print("БД =", row[1])
print()
print('БД "users": ')
cursor.copy_to(sys.stdout, 'users', sep='\t', )

