from db.db_connection import DBConnection
import colorama as cl
db = DBConnection()



def fetch_faq():
    """FAQ tablosundan tüm soru-cevap çiftlerini getirir."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT question, answer FROM faq;")
            data = cur.fetchall()
        print(f"{cl.Fore.GREEN}FAQ fetched successfully{cl.Style.RESET_ALL}")
        conn.close()
        return data
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")
        return None

def insert_faq(question, answer):
    """FAQ tablosuna yeni bir soru-cevap çifti ekler."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO faq (question, answer) VALUES (%s, %s);",
                (question, answer)
            )
        print(f"{cl.Fore.GREEN}FAQ inserted successfully{cl.Style.RESET_ALL}")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")

def delete_faq(question):
    """FAQ tablosundan belirli bir soru-cevap çiftini siler."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM faq WHERE question = %s;", (question,))
        print(f"{cl.Fore.GREEN}FAQ deleted successfully{cl.Style.RESET_ALL}")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")

def fetch_personal_info(key):
    """Belirli bir kişisel bilgiyi getirir."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT info_value FROM personal_data WHERE info_key = %s;", (key,))
            data = cur.fetchone()
        print(f"{cl.Fore.GREEN}Personal info fetched successfully{cl.Style.RESET_ALL}")
        conn.close()
        return data
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")
        return None


def insert_personal_info(key, value):
    """Kişisel bilgi ekler veya günceller."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO personal_data (info_key, info_value) VALUES (%s, %s) "
                "ON CONFLICT (info_key) DO UPDATE SET info_value = %s;",
                (key, value, value)
            )
        print(f"{cl.Fore.GREEN}Personal info inserted successfully{cl.Style.RESET_ALL}")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")

def delete_personal_info(key):
    """Belirli bir kişisel bilgiyi siler."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM personal_data WHERE info_key = %s;", (key,))
        print(f"{cl.Fore.GREEN}Personal info deleted successfully{cl.Style.RESET_ALL}")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")
def fetch_expenses():
    """Harcama tablosundan tüm kayıtları getirir."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT date, amount, description FROM expenses;")
            data = cur.fetchall()
        print(f"{cl.Fore.GREEN}Expenses fetched successfully{cl.Style.RESET_ALL}")
        conn.close()
        return data
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")
        return None

def insert_expense(date, amount, description):
    """Harcama tablosuna yeni kayıt ekler."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO expenses (date, amount, description) VALUES (%s, %s, %s);",
                (date, amount, description)
            )
        print(f"{cl.Fore.GREEN}Expense inserted successfully{cl.Style.RESET_ALL}")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")

def delete_expense(date):
    """Harcama tablosundan belirli bir kaydı siler."""
    try:
        conn = db.get_connection()
        with conn.cursor() as cur:
            cur.execute("DELETE FROM expenses WHERE date = %s;", (date,))
        print(f"{cl.Fore.GREEN}Expense deleted successfully{cl.Style.RESET_ALL}")
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"{cl.Fore.RED}Error: {e}{cl.Style.RESET_ALL}")
