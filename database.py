import psycopg2
from PyQt5.QtGui import QStandardItem
from psycopg2 import sql
import subprocess
import os

info_dbname = 'anime_merch'
info_user = 'postgres'
info_password = '67admin45'
info_host = 'localhost'
info_port = '5432'

def restore_database(user, password, dbname, host, port):
    psql_path = r'C:\Program Files\PostgreSQL\17\bin\psql.exe'
    sql_file_path = 'anime_merch.sql'

    # Установка переменной окружения для пароля
    os.environ['PGPASSWORD'] = password

    # Вызов psql
    result = subprocess.run(
        [psql_path, '-U', user, '-d', dbname, '-h', host, '-p', port, '-f', sql_file_path],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def save_database(user, password, dbname, host, port):
    pg_dump_path = r'C:\Program Files\PostgreSQL\17\bin\pg_dump.exe'  # Замените на ваш путь
    backup_file_path = 'anime_merch.sql'
    os.environ['PGPASSWORD'] = password

    # Команда для создания бэкапа в формате SQL

    result = subprocess.run(
        [pg_dump_path, '-U', user, '-h', host, '-p', port, '-f', backup_file_path, dbname],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

def ensure_db_exists(dbname):
    conn = psycopg2.connect(
        dbname='postgres',
        user= info_user,
        password= info_password,
        host= info_host,
        port= info_port
    )
    conn.autocommit = True
    cursor = conn.cursor()

    # Проверка, существования БД
    cursor.execute(sql.SQL("SELECT 1 FROM pg_database WHERE datname = %s"), [dbname])
    exists = cursor.fetchone()

    # Если БД не существует
    if not exists:
        cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier(dbname)))
        restore_database(info_user, info_password, dbname, info_host, info_port)

    cursor.close()
    conn.close()

def connect_db():
    ensure_db_exists(info_dbname)
    conn = psycopg2.connect(
        dbname= info_dbname,
        user= info_user,
        password= info_password,
        host= info_host,
        port= info_port
    )
    cursor = conn.cursor()
    return cursor, conn

def load_data_from_db(model, name_table):
    cursor, conn = connect_db()

    if name_table == 'anime_table':
        # Выполнение SQL запроса
        cursor.execute("SELECT a_name FROM anime;")
        rows = cursor.fetchall()

        model.clear()
        # Добавьте данные в модель
        for index, row in enumerate(rows):
            model.appendRow([
                QStandardItem(str(index + 1)),  # Номер
                QStandardItem(row[0]),  # Наименование
                QStandardItem()  # Ячейка для кнопок или других действий
            ])

    elif name_table == 'product_table':
        # Выполнение SQL запроса
        model.clear()
        cursor.execute("""SELECT p_name, a.a_name, p_price, p_count
                        FROM product p
                        JOIN anime a ON p.p_anime = a.id_anime;""")
        rows = cursor.fetchall()

        # Добавьте данные в модель
        for index, row in enumerate(rows):
            model.appendRow([
                QStandardItem(str(index + 1)),  # Номер
                QStandardItem(row[0]),  # Наименование продукта
                QStandardItem(row[1]),  # Наименование аниме
                QStandardItem(f"{row[2]:.2f}"),  # Цена
                QStandardItem(str(row[3]))  # Количество
            ])

    cursor.close()
    conn.close()

def add_to_database_product(name, anime, price, count):
    if name and anime and price and count:  # Проверка, что все поля заполнены
        cursor, conn = connect_db()

        # Получаем ID аниме
        cursor.execute("SELECT id_anime FROM anime WHERE a_name = %s;", (anime,))
        anime_id = cursor.fetchone()

        if anime_id is None:  # Если аниме не найдено
            cursor.close()
            conn.close()
            return False

        # Извлекаем ID из кортежа
        anime_id = anime_id[0]

        # Приводим price и count к нужным типам данных, если это необходимо
        price = float(price)  # Убедитесь, что цена - это число
        count = int(count)    # Убедитесь, что количество - это целое число

        # SQL-запрос для вставки данных
        cursor.execute("""
            INSERT INTO product (p_name, p_anime, p_price, p_count) 
            VALUES (%s, %s, %s, %s)
        """, (name, anime_id, price, count))

        # Сохранение изменений
        conn.commit()

        cursor.close()
        conn.close()

        return True

def add_to_database_anime(name):
    if name:  # Проверка, что все поля заполнены
        cursor, conn = connect_db()

        # SQL-запрос для вставки данных
        cursor.execute("""
                INSERT INTO anime (a_name) 
                VALUES (%s)
        """, (name,))

        # Сохранение изменений
        conn.commit()

        cursor.close()
        conn.close()

def delete_anime_by_name(anime_name):
    cursor, conn = connect_db()

    cursor.execute("DELETE FROM anime WHERE a_name = %s;", (anime_name,))
    conn.commit()

    cursor.close()
    conn.close()

def delete_product(name, anime, price, count):
    cursor, conn = connect_db()

    cursor.execute("SELECT id_anime FROM anime WHERE a_name = %s;", (anime,))
    anime_id = cursor.fetchone()
    anime_id = anime_id[0]

    cursor.execute("""
            DELETE FROM product 
            WHERE p_name = %s AND p_anime = %s AND p_price = %s AND p_count = %s
        """, (name, anime_id, price, count))
    conn.commit()

    cursor.close()
    conn.close()
