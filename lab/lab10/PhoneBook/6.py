import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='postgres',    
    password='Nurtiley17'
)

current = config.cursor()

# запрос id, name, number по отсортированному имени 
sql1 = '''
    SELECT id, name, number FROM phonebook ORDER BY name ASC
'''
# запрос номера телефона определенного человека 
sql2 = '''
    SELECT number FROM phonebook WHERE name = 'Nurtileu'
'''
current.execute(sql2)

final = current.fetchall()
print(final)
current.close()
config.commit()
config.close()