import psycopg2
import csv

# Database config
DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASSWORD = "12345678"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

def create_table():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook (
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(100),
                    phone VARCHAR(20) UNIQUE NOT NULL
                );
            """)
            conn.commit()
            print("Таблица создана.")

def insert_from_console():
    name = input("Введите имя: ")
    phone = input("Введите номер телефона: ")
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (name, phone))
                conn.commit()
                print("Контакт добавлен.")
    except Exception as e:
        print("Ошибка:", e)

def insert_from_csv(csv_file):
    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                with open(csv_file, newline='', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    for row in reader:
                        try:
                            cur.execute("INSERT INTO phonebook (first_name, phone) VALUES (%s, %s)", (row[0], row[1]))
                        except Exception as e:
                            print(f"Ошибка при добавлении {row}: {e}")
                conn.commit()
                print("Импорт завершён.")
    except Exception as e:
        print("Ошибка подключения:", e)

def update_data():
    phone = input("Введите номер телефона для обновления: ")
    new_name = input("Новое имя (или пропустите): ")
    new_phone = input("Новый номер телефона (или пропустите): ")

    query_parts = []
    values = []

    if new_name:
        query_parts.append("first_name = %s")
        values.append(new_name)
    if new_phone:
        query_parts.append("phone = %s")
        values.append(new_phone)

    if not query_parts:
        print("Нет данных для обновления.")
        return

    values.append(phone)

    query = f"UPDATE phonebook SET {', '.join(query_parts)} WHERE phone = %s"

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(query, values)
                if cur.rowcount:
                    print("Обновление выполнено.")
                else:
                    print("Контакт не найден.")
                conn.commit()
    except Exception as e:
        print("Ошибка:", e)

def query_data():
    print("Фильтрация: 1 - по имени, 2 - по номеру, 3 - все контакты")
    choice = input("Выбор: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if choice == "1":
                    name = input("Введите имя: ")
                    cur.execute("SELECT * FROM phonebook WHERE first_name ILIKE %s", (f"%{name}%",))
                elif choice == "2":
                    phone = input("Введите номер: ")
                    cur.execute("SELECT * FROM phonebook WHERE phone LIKE %s", (f"%{phone}%",))
                else:
                    cur.execute("SELECT * FROM phonebook")

                rows = cur.fetchall()
                for row in rows:
                    print(row)
    except Exception as e:
        print("Ошибка:", e)

def delete_data():
    print("Удалить по: 1 - имени, 2 - номеру")
    choice = input("Выбор: ")

    try:
        with get_connection() as conn:
            with conn.cursor() as cur:
                if choice == "1":
                    name = input("Введите имя: ")
                    cur.execute("DELETE FROM phonebook WHERE first_name = %s", (name,))
                elif choice == "2":
                    phone = input("Введите номер: ")
                    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
                else:
                    print("Неверный выбор.")
                    return

                if cur.rowcount:
                    print("Контакт удалён.")
                else:
                    print("Контакт не найден.")
                conn.commit()
    except Exception as e:
        print("Ошибка:", e)

def main_menu():
    create_table()

    while True:
        print("\nМеню:")
        print("1. Добавить контакт (ручной ввод)")
        print("2. Импорт из CSV")
        print("3. Обновить контакт")
        print("4. Поиск")
        print("5. Удалить контакт")
        print("0. Выход")

        choice = input("Выбор: ")
        if choice == "1":
            insert_from_console()
        elif choice == "2":
            csv_path = input("Путь к CSV: ")
            insert_from_csv(csv_path)
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "0":
            print("Выход...")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main_menu()