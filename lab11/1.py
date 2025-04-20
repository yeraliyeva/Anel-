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

# Функция поиска по шаблону
def search_phonebook(pattern):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, first_name, phone FROM phonebook WHERE first_name ILIKE %s OR phone ILIKE %s", 
                ('%' + pattern + '%', '%' + pattern + '%'))
    for record in cur.fetchall():
        print(f"ID: {record[0]}, Name: {record[1]}, Phone: {record[2]}")
    cur.close()
    conn.close()

# Пример использования
search_phonebook("mama")
