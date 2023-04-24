import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='postgres',    
    password='Nurtiley17'
)
# удаление данных по имени или по номеру
current = config.cursor()
del_data = input("By what do you want to delete?: ")
del_data = del_data.lower()
temp = input(f'Which {del_data} do you want to delete?: ')
if del_data == 'name':
    sql = '''
        DELETE FROM phonebook WHERE name = %s RETURNING *
    '''
elif del_data == 'number':
    sql = '''
        DELETE FROM phonebook WHERE number = %s RETURNING *
    '''
current.execute(sql, (temp,))
config.commit()
current.close()
config.close()