import colorama as cl
import psycopg2
from psycopg2.extras import RealDictCursor
import dotenv as de
import os

de.load_dotenv()

class DBConnection:
    _instance = None
    _first_connection = True

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(DBConnection, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    def get_connection(self):

            connection = psycopg2.connect(
                dbname=self.db_name,
                user=self.db_user,
                password=self.db_password,
                host=self.db_host,
                port=self.db_port
            )
            if DBConnection._first_connection:
                print(f"{cl.Fore.GREEN}Connection successful{cl.Style.RESET_ALL}")
                DBConnection._first_connection = False
            return connection
    def get_dict_cursor(self):
        try:
            connection = self.get_connection()
            cursor = connection.cursor(cursor_factory=RealDictCursor)
            print(f'{cl.Fore.GREEN}Cursor created successful{cl.Style.RESET_ALL}')
            return cursor
        except Exception as e:
            print(f'{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}')
            return None

    def close_connection(self, connection):
        connection.close()
        print(f'{cl.Fore.LIGHTGREEN_EX}Connection closed successful{cl.Style.RESET_ALL}')


