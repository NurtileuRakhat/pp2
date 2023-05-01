import telebot,os,psycopg2
from telebot import types 
from dotenv import load_dotenv

config = psycopg2.connect(
    host='localhost', 
    database='Telegram_bot',
    user='postgres',    
    password='Nurtiley17'
)
cursor = config.cursor()

load_dotenv('.env')
TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Define the menu commands
menu_commands = [
    telebot.types.BotCommand('start', 'Start the bot'),
    telebot.types.BotCommand('help', 'Get help'),
    telebot.types.BotCommand('about', 'About the bot'),
    telebot.types.BotCommand('update', 'add to the database')
]

def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu

def insert_data(id:int, username:str, us_name:str,us_sname:str,phonenumber:str,chatid:int):
	sql = '''INSERT INTO test(id, username, us_name,us_sname,phonenumber,chatid) VALUES (%s, %s, %s, %s, %s, %s)'''
	cursor.execute(sql, (id, username, us_name,us_sname,phonenumber,chatid))
	config.commit()

# Define a handler for the /start command
@bot.message_handler(commands=['start']) 
def start(message):
    buttons_list = [
    types.InlineKeyboardButton("add new phone number:", callback_data = 'number'),
    types.InlineKeyboardButton("All contacts:", callback_data = 'all_contact'),
    ]   

    reply_markup = types.InlineKeyboardMarkup(build_menu(buttons_list, n_cols=2))

    bot.send_message(message.chat.id,'choose command:' , reply_markup=  reply_markup)

# Define a handler for the /help command
@bot.message_handler(commands=['help'])
def help(message):
    message_text = "Here are my commands:\n\n"
    for command in menu_commands:
        message_text += f"/{command.command} - {command.description}\n"
    bot.reply_to(message, message_text)

# Define a handler for the /about command
@bot.message_handler(commands=['about']) 
def about(message):
    buttons_list = [
    types.InlineKeyboardButton("Nurtileu Rakhat", url='https://t.me/nurtileurk'),
    types.InlineKeyboardButton("GitHub", url='https://github.com/NurtileuRakhat')
    ]   

    reply_markup = types.InlineKeyboardMarkup(build_menu(buttons_list, n_cols=2))

    bot.send_message(message.chat.id,'Create by' , reply_markup=  reply_markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == 'number':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        markup.add(types.KeyboardButton('Send phone number', request_contact=True))
        bot.send_message(call.message.chat.id, "Please send me your phone number", reply_markup=markup)
        
    elif call.data == 'all_contact':
        # Table data query
        cursor.execute("SELECT us_name, phonenumber FROM test;")
        rows = cursor.fetchall()
 
        # Data processing and message formation
        message = "Data from the table:\n"
        for row in rows:
            message += f"{row[0]}: {row[1]}\n"

        # Sending a Message to Chat
        bot.send_message(call.message.chat.id, message)

# Receive Phone Number Handler
@bot.message_handler(content_types=['contact'])
def contact(message):
    global number
    # Check that the message contains a phone number
    if message.contact is not None: 
        number = message.contact.phone_number
        bot.send_message(message.chat.id, "successful")
     
@bot.message_handler(commands=['update'])
def get_text_messages(message):
	bot.send_message(message.chat.id, 'Your contact is added to the database!')
        
	id = message.from_user.id
	username = message.from_user.username
	us_name = message.from_user.first_name
	us_sname = message.from_user.last_name   
	phonenumber = number
	chatid = message.chat.id
		
	insert_data(id = id, username=username,us_name=us_name,us_sname=us_sname,phonenumber=phonenumber, chatid=chatid)

# Set the menu commands for the bot
bot.set_my_commands(menu_commands)

# Start the bot
bot.polling(none_stop=True)