import db.db_operations as db
import colorama as cl

'''
TEST DATABASE OPERATIONS
'''

# Test inserting faq
try:
    db.insert_faq('Test question', 'Test answer')
    db.delete_faq('Test question') # Clean up
except Exception as e:
    print(f'{cl.Fore.YELLOW}Error: {e}{cl.Style.RESET_ALL}')

# Test fetching faq
try:
    faq = db.fetch_faq()
except Exception as e:
    print( f'{cl.Fore.YELLOW}Error: {e}{cl.Style.RESET_ALL}')

# Test inserting personal info
try:
    db.insert_personal_info('Test key', 'Test value')
    db.delete_personal_info('Test key') # Clean up
except Exception as e:
    print(f'{cl.Fore.YELLOW}Error: {e}{cl.Style.RESET_ALL}')

# Test fetching personal info
try:
    personal_info = db.fetch_personal_info('Test key')
except Exception as e:
    print(f'{cl.Fore.YELLOW}Error: {e}{cl.Style.RESET_ALL}')

# Test updating personal info




