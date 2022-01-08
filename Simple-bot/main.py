import telebot
from telebot import types
token = '...'
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup()
    keyboard.row("сайт", "эиос", "vk", "/help")
    bot.send_message(message.chat.id, 'Привет! Какую информацию о МТУСИ хочешь узнать?', reply_markup=keyboard)
@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, '/MyID - узнай свой ID в Telegram\n' +
                     '/bvt2107 - список группы БВТ2107\n' +
                     '/Starosta - староста в telegram')
@bot.message_handler(commands = ['MyID'])
def MyID(message):
    bot.send_message(message.chat.id, str(message.chat.id))
@bot.message_handler(commands = ['bvt2107'])
def bvt2107(message):
    doc = open('templates/бвт2107.docx', 'rb')
    bot.send_document(message.chat.id, doc)
    bot.send_document(message.chat.id, "FILEID")
@bot.message_handler(commands = ['Starosta'])
def Starosta(message):
    bot.send_message(message.chat.id, '@Lissa2405')
@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text.lower() == "сайт":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://mtuci.ru/')
    elif message.text.lower() == "эиос":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://lms.mtuci.ru/')
    elif message.text.lower() == "vk":
        bot.send_message(message.chat.id, 'Тогда тебе сюда – https://vk.com/mtuci')


bot.polling()