import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='Telegram_bot',
    user='postgres',    
    password='Nurtiley17'
)

current = config.cursor()
sql = '''
        CREATE TABLE test(
            id VARCHAR(),
            username VARCHAR(100),
            us_name VARCHAR(100),
            us_sname VARCHAR(100),
            phoneNumber VARCHAR(12),
            chatid VARCHAR,
            UNIQUE(chatid)
    );
''' 

current.execute(sql)

current.close()
config.commit()
config.close()