import numpy as np
import db.db_connection as db
import utils.preprocessing as pre
import utils.fastSim as fs
import colorama as cl

# Veritabanı bağlantısı
db = db.DBConnection()
entity_intent_finder = fs.FastTextEntityIntent(model_path='wiki.tr.txt',sentences_corpus_size=3000)
# Veritabanı bağlantısını aç
connection = db.get_connection()
while True:
    user_input = input(cl.Fore.LIGHTMAGENTA_EX + "Enter a question: ")
    if user_input == "exit":
        break

    intents_n = []
    intents_d = []
    intents_i = []
    query = "SELECT id,name,description FROM intent_table"
    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    for intent in result:
        intents_n.append(intent[1])
        intents_d.append(intent[2])
        intents_i.append(intent[0])

    #
    #  Intent belirleme

    valid_in = entity_intent_finder.find_entities(user_input, intents_n)
    if valid_in in intents_n:
        valid_in_index = intents_n.index(valid_in)
    else:
        print("No valid intent found.")
        continue

    print("Valid Intents: ", valid_in)
    # Entity belirleme

    entity = []
    entity_i = []
    query ='''
    SELECT id,entity_name
    FROM entity_table
    WHERE intent_id = %s;
    '''
    cursor.execute(query, (intents_i[valid_in_index],))
    result = cursor.fetchall()
    for r in result:
        entity.append(r[1])
        entity_i.append(r[0])

    # Entity  belirleme
    valid_en = entity_intent_finder.find_entities(user_input, entity)
    if valid_en in entity:
        valid_en_index = entity.index(valid_en)
    else:
        print("No valid entity found.")
        continue

    print("Valid Entities: ", valid_en)

    # Response belirleme
    query = "SELECT response FROM response_pool WHERE intent_id = %s AND entity_id = %s"
    cursor.execute(query, (intents_i[valid_in_index], entity_i[valid_en_index]))
    response = cursor.fetchall()
    if response:
        print(cl.Fore.YELLOW + cl.Style.BRIGHT +f'Question: {user_input}')
        print(cl.Fore.CYAN + f"Responses: {response}")
    else:
        print("No response found.")
    cursor.close()