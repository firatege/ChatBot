import db.db_connection as db_conn
import colorama as cl

''' 
TEST CONNECTION TO DATABASE 
'''


# Test connection to database
try:
    connection = db_conn.DBConnection().get_connection()
    if connection is None:
        print(f'{cl.Fore.CYAN}Connection failed{cl.Style.RESET_ALL}')
except Exception as e:
    print(f'{cl.Fore.YELLOW}Error: {e}{cl.Style.RESET_ALL}')

# Test cursor creation

try:
    cursor = db_conn.DBConnection().get_dict_cursor()
    if cursor is None:
        print(f'{cl.Fore.CYAN}Cursor creation failed{cl.Style.RESET_ALL}')
except Exception as e:
    print(f'{cl.Fore.YELLOW}Error: {e}{cl.Style.RESET_ALL}')

# Test closing connection
try:
    connection = db_conn.DBConnection().get_connection()
    db_conn.DBConnection().close_connection(connection)
except Exception as e:
    print(f'{cl.Fore.YELLOW}Error: {e}{cl.Style.RESET_ALL}')

