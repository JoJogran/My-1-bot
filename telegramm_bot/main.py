import telebot,random

bot = telebot.TeleBot("7088195729:AAHk0j2D13RFhL8djAXFuRpQIE64F2RyRu0")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Список команд" )
    bot.reply_to(message, "1) /hello" )
    bot.reply_to(message, "2) /bye" )
    bot.reply_to(message, "3) /mem" )
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")

@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")
@bot.message_handler(commands=['mem'])
def send_mem(message):
    cisl = random.randint(1,10)
    if cisl == 1:
        with open('images/MEM1.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)  
    elif cisl == 2:
        with open('images/MEM2.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif cisl == 3:
         with open('images/MEM3.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif cisl == 4:
         with open('images/MEM4.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif cisl == 5:
         with open('images/MEM5.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif cisl == 6:
         with open('images/MEM6.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif cisl == 7:
         with open('images/MEM7.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif cisl == 8:
         with open('images/MEM8.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif cisl == 9:
         with open('images/MEM9.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
    elif cisl == 10:
         with open('images/MEM10.jpg', 'rb') as f:  
            bot.send_photo(message.chat.id, f)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()