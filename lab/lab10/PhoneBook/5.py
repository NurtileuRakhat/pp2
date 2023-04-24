import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='sampledb',
    user='postgres',    
    password='Nurtiley17'
)
current = config.cursor()
# обновление данных в таблице 
user_id = int(input("Enter ID: "))
change = input("What do you want to change?: ")
change = change.lower()
data = input(f'To what value set the {change}?: ')
if change == 'name':
    sql = '''
        UPDATE phonebook SET name = %s WHERE id = %s;
    '''
elif change == 'number':
    sql = '''
        UPDATE phonebook SET number = %s WHERE id = %s;
    '''
current.execute(sql, (data, user_id))
config.commit()
current.close()
config.close()