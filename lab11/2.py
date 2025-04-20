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
