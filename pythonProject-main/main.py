import telebot
import datetime
from telebot import types
from telegram_bot_calendar import DetailedTelegramCalendar, LSTEP
bot = telebot.TeleBot('6189070272:AAGodOjSPW6u-Vg_rcvktvJmq3hsshzxRb8')

@bot.message_handler(commands=['s'])
def start(m):
    calendar, step = DetailedTelegramCalendar().build()
    bot.send_message(m.chat.id,
                     f"Select {LSTEP[step]}",
                     reply_markup=calendar)


@bot.callback_query_handler(func=DetailedTelegramCalendar.func())
def cal(c):
    result, key, step = DetailedTelegramCalendar().process(c.data)
    if not result and key:
        bot.edit_message_text(f"Select {LSTEP[step]}",
                              c.message.chat.id,
                              c.message.message_id,
                              reply_markup=key)
    elif result:
        bot.edit_message_text(f"You selected {result}",
                              c.message.chat.id,
                              c.message.message_id)
        # в result хранится дата куда чел нажал m типа массив врменный куда сохраняем дату его заезда и выезда
        m.append(result)

m=[]
#reserv типа база данных дата броней
reserv=[]
reserv=[(datetime.date(2023, 2, 5),(datetime.date(2023, 2, 8)))]
# херня временая забей
@bot.message_handler(commands=['h'])
def start_message(message):
    for item in m:
        bot.send_message(message.chat.id,item)
#функция проверки свободно или нет эта дата
@bot.message_handler(commands=['check'])
def start_message(message):
    flag=True
    for item in reserv:
        if item[0]==m[0] or item[1]==m[1] or (item[0]>m[0] and item[0]<m[1]) or ( item[1]<m[1] and item[1]>m[0]):
            bot.send_message(message.chat.id, 'свободно')
        else:
            bot.send_message(message.chat.id, ' не свободно')

@bot.message_handler(commands=['help', 'start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет')

@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Квартиры")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)
@bot.message_handler(content_types='text')
def welcome(message):
    if message.text == "Квартиры":
        text="""Квартира с Евро ремонтом рядом с Ривьерой   \
         Адрес: Сибгата Хакима 60 \
         Цена: от 1.600 \
         Спальных мест: 4   \
         Кол-во комнат: 2"""
        text2 = """Уютная квартира рядом с Корстоном    \
         Адрес: Гвардейская 7 \
         Цена: от 1.200 \
         Спальных мест: 5   \
         Кол-во комнат: 2"""
        text3 = """Квартира рядом с центром города \
                 Адрес: Татарстан 66 \
                 Цена: от 1.200 \
                 Спальных мест: 5   \
                 Кол-во комнат: 2"""

        with open('img1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text)
        with open('img1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text2)
        with open('img1.png', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text3)
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("1")
        item3 = types.KeyboardButton("2")
        item4 = types.KeyboardButton("3")
        markup2.add(item2)
        markup2.add(item3)
        markup2.add(item4)
        bot.send_message(message.chat.id, 'Выберите квартиру:', reply_markup=markup2)
        #Тут выбор квартиры крч
        if message.text == "1":
            text11 = """Квартира с Евро ремонтом рядом с Ривьерой   \
                    Адрес: Сибгата Хакима 60 \
                    Цена: от 1.600 \
                    Спальных мест: 4   \
                    Кол-во комнат: 2"""
            with open('img1.png', 'rb') as photo:
                bot.send_photo(message.chat.id, photo, caption=text)
            item2 = types.KeyboardButton("Фото")
            item3 = types.KeyboardButton("Описание")
            item4 = types.KeyboardButton("Забронировать/посмотреть даты")
            markup2.add(item2)
            markup2.add(item3)
            markup2.add(item4)

bot.infinity_polling()