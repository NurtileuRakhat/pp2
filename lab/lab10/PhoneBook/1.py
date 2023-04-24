import psycopg2
# создаем таблицу телефонной книги
config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='postgres',    
    password='Nurtiley17'
)

current = config.cursor()
sql = '''
        CREATE TABLE phonebook(
            id INTEGER PRIMARY KEY,
            name VARCHAR(100),
            number VARCHAR(12)
    );
'''
current.execute(sql)

current.close()
config.commit()
config.close()