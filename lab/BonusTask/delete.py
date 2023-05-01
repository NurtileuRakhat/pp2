import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='Telegram_bot',
    user='postgres',    
    password='Nurtiley17'
)
# удаление данных по id или по username
current = config.cursor()
del_data = input("By what do you want to delete?: ")
del_data = del_data.lower()
temp = input(f'Which {del_data} do you want to delete?: ')
if del_data == 'id':
    sql = '''
        DELETE FROM test WHERE id = %s RETURNING *
    '''
elif del_data == 'username':
    sql = '''
        DELETE FROM test WHERE username = %s RETURNING *
    '''
current.execute(sql, (temp,))
config.commit()
current.close()
config.close()