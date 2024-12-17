import psycopg2
from psycopg2 import sql
import subprocess
import os

info_dbname = 'anime_merch'  # Подключаемся к стандартной базе данных
info_user = 'postgres'
info_password = '67admin45'
info_host = 'localhost'
info_port = '5432'

def restore_database(user, password, dbname, host, port):
    # Путь к psql.exe
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
    # Укажите полный путь к pg_dump.exe
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
    # Подключаемся к стандартной базе данных postgres для выполнения операций
    conn = psycopg2.connect(
        dbname='postgres',  # Подключаемся к стандартной базе данных
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

def connect_db(dbname):
    ensure_db_exists(dbname)
    conn = psycopg2.connect(
        dbname= dbname,
        user= info_user,
        password= info_password,
        host= info_host,
        port= info_port
    )
    return conn
