import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='Telegram_bot',
    user='postgres',    
    password='Nurtiley17'
)

current = config.cursor()
sql = '''
        CREATE TABLE bot_PP2(
            id INTEGER PRIMARY KEY,
            username VARCHAR(100),
            us_name VARCHAR(100),
            us_sname VARCHAR(100),
            phoneNumber VARCHAR(12),
            chatid INT,
            UNIQUE(chatid)
    );
''' 

current.execute(sql)

current.close()
config.commit()
config.close()