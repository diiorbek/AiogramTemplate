import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname=os.getenv('DATABASE_NAME'),
            user=os.getenv('DATABASE_USER'),
            password=os.getenv('DATABASE_PASSWORD'),
            host=os.getenv('DATABASE_HOST'),
            port=os.getenv('DATABASE_PORT')
        )
        self.cursor = self.conn.cursor()

    def close_connection(self):
        self.cursor.close()
        self.conn.close()

    def add_user(self, telegram_id, telegram_username, full_name):
        query = """
        INSERT INTO "Actions_botusers" (telegram_id, telegram_username, full_name)
        VALUES (%s, %s, %s)
        ON CONFLICT (telegram_id) DO NOTHING;
        """
        try:
            self.cursor.execute(query, (telegram_id, telegram_username, full_name))
            self.conn.commit()
            print(f"User {full_name} added successfully!")
        except Exception as e:
            self.conn.rollback()
            print(f"Error adding user: {e}")

    def select_all_users(self):
        sql = """
        SELECT * FROM "Actions_botusers";
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def select_user(self, **kwargs):
        sql = """SELECT * FROM "Actions_botusers" WHERE """
        conditions = []
        parameters = []
        for key, value in kwargs.items():
            conditions.append(f"{key} = %s")
            parameters.append(value)
        sql += " AND ".join(conditions)
        self.cursor.execute(sql, parameters)
        return self.cursor.fetchone()

    def count_users(self):
        self.cursor.execute("""SELECT COUNT(*) FROM "Actions_botusers";""")
        return self.cursor.fetchone()

    def delete_users(self):
        self.cursor.execute("""DELETE FROM "Actions_botusers" WHERE TRUE;""")
        self.conn.commit()

    def all_users_id(self): 
        self.cursor.execute("""SELECT telegram_id FROM "Actions_botusers";""")
        return self.cursor.fetchall()

    def list_tables(self):
        # Запрос для получения всех таблиц в базе данных
        query = """
        SELECT table_schema, table_name
        FROM information_schema.tables
        WHERE table_type = 'BASE TABLE'
          AND table_schema NOT IN ('pg_catalog', 'information_schema')
        ORDER BY table_schema, table_name;
        """
        self.cursor.execute(query)
        tables = self.cursor.fetchall()
        
        # Проверяем, что запрос вернул данные
        if tables:
            return tables
        else:
            print("No tables found.")
            return None
