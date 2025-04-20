import psycopg2

# Конфигурация базы данных
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "12345678"
DB_HOST = "localhost"
DB_PORT = "5432"

# Функция для получения соединения
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT
    )

# Вставка нескольких пользователей
def insert_multiple_users(names, phones):
    conn = get_connection()
    cur = conn.cursor()
    
    # Вызов хранимой процедуры
    cur.execute("CALL insert_multiple_users(%s, %s)", (names, phones))
    
    # Применяем изменения в базе
    conn.commit()
    
    # Получаем и выводим все уведомления (например, некорректные данные)
    cur.execute("SELECT * FROM pg_catalog.pg_listener WHERE condition = 'NOTICE';")
    notifications = cur.fetchall()
    for notification in notifications:
        print(notification)
    
    cur.close()
    conn.close()

# Пример использования
names = ["mama","Anel"]
phones = [ "87773683978", "1233455"]

insert_multiple_users(names, phones)
import psycopg2
datab = psycopg2.connect(
    dbname="phonebook_db",
    user="postgres",
    password="postgres1234",  
    host="localhost"
)
cur = datab.cursor()
def search():
    pattern = input("name or phone: ")
    cur.execute("SELECT * FROM phonebook WHERE username ILIKE %s OR phone::TEXT ILIKE %s;", 
                ('%' + pattern + '%', '%' + pattern + '%'))
    for row in cur.fetchall():
        print(row)
def insert_or_update_user():
    name = input("name: ")
    new_phone = input("new phone: ")

    cur.execute("CALL insert_or_update_user(%s::TEXT, %s::BIGINT);", (name, new_phone))
    datab.commit()
# phonebook_db=# CREATE OR REPLACE PROCEDURE insert_or_update_user(name VARCHAR, new_phone VARCHAR)
# phonebook_db-# AS $$
# phonebook_db$# BEGIN
# phonebook_db$#
# phonebook_db$#     IF EXISTS (SELECT 1 FROM phonebook WHERE username = name) THEN
# phonebook_db$#         UPDATE phonebook SET phone = new_phone WHERE username = name;
# phonebook_db$#     ELSE
# phonebook_db$#         INSERT INTO phonebook (username, phone) VALUES (name, new_phone);
# phonebook_db$#     END IF;
# phonebook_db$# END;
# phonebook_db$# $$ LANGUAGE plpgsql;
def bulk_insert_users():
    lst = [
        ["Amina", "87010168877"],
        ["Altair", "87020691626"],
        ["Arssen", "87780027978"]
    ]
    for user in lst:
      cur.execute("CALL insert_lst(%s, %s)", (user[0], user[1]))
    datab.commit()
bulk_insert_users()
# CREATE OR REPLACE PROCEDURE insert_lst(name VARCHAR, phone VARCHAR) AS
# $$
# BEGIN 
#     INSERT INTO phonebook (username, phone)
#         VALUES (name, phone);
# END;
# $$ LANGUAGE plpgsql;
def pegin():
    limit=int(input("limit: "))
    offset=int(input("offset: "))
    cur.execute("SELECT * FROM phonebook LIMIT %s OFFSET %s;", (limit, offset))
    results = cur.fetchall()
    for row in results:
        print(row)
#pegin()
def delete():
    pattern=input("name or phone: ").strip()
    cur.execute("CALL delete(%s, %s);", (pattern, pattern))
    datab.commit()
#delete()
# CREATE OR REPLACE PROCEDURE delete(name VARCHAR, phoned VARCHAR)
# AS $$
# BEGIN
#     DELETE FROM phonebook
#     WHERE ( username = name)
#        OR ( phone = phoned);
# END;
# $$ LANGUAGE plpgsql;
#search()
#insert_or_update_user()
cur.close()
datab.close()