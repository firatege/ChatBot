from db.db_connection import DBConnection
import colorama as cl
db = DBConnection()


def get_entities():
    try:
        conn = db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM entity_table")
        entities = cursor.fetchall()
        return entities
    except Exception as e:
        print(f'{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}')
        return None


