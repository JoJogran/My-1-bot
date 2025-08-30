import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TELEGRAM_TOKEN = '7088195729:AAHk0j2D13RFhL8djAXFuRpQIE64F2RyRu0'

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("1/5", callback_data="cb_yes"),
                               InlineKeyboardButton("2/5", callback_data="cb_no"),
                                InlineKeyboardButton("3/5", callback_data="cb_o"),
                                InlineKeyboardButton("4/5", callback_data="cb_4"),
                                InlineKeyboardButton("5/5", callback_data="cb_5"))
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "cb_yes":
        bot.answer_callback_query(call.id, "...")
    elif call.data == "cb_no":
        bot.answer_callback_query(call.id, "Ну...Ладно...")
    elif call.data == "cb_o":
        bot.answer_callback_query(call.id, "Спаибо конечно,ноо...")
    elif call.data == "cb_4":
        bot.answer_callback_query(call.id, "Спасибочкии")
    elif call.data == "cb_5":
        bot.answer_callback_query(call.id, "Ого,спасибоооо")


@bot.message_handler(func=lambda message: True)
def message_handler(message):
    bot.send_message(message.chat.id, "Как тебе мой бот?", reply_markup=gen_markup())

bot.infinity_polling()