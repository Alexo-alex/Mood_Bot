from telebot import types, TeleBot

# Це наш токен
TOKEN = ' ваш токен'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i_am_roll = types.KeyboardButton(text='Рофлю 🤣')
    i_am_joyful = types.KeyboardButton(text='Радію 🙂')
    i_am_angry = types.KeyboardButton(text='Агрюсь 😡')
    i_am_norms = types.KeyboardButton(text='Норм 😑')

    markup_inline.add(i_am_roll, i_am_joyful, i_am_angry, i_am_norms)
    bot.send_message(message.chat.id, 'Обери свій муд на сьогодні!', reply_markup=markup_inline)


@bot.message_handler(content_types=['text'])
def get_text(message):
    text = message.text
    if 'Рофлю' in text:
        sti_1 = open('static/Laughs_to_tears.png', 'rb')
        bot.send_sticker(message.chat.id, sti_1)
    elif 'Радію' in text:
        sti_1 = open('static/Cheerful.png', 'rb')
        bot.send_sticker(message.chat.id, sti_1)
    elif 'Агрюсь' in text:
        sti_1 = open('static/Angry.png', 'rb')
        bot.send_sticker(message.chat.id, sti_1)
    elif 'Норм' in text:
        sti_1 = open('static/Poker_face.png', 'rb')
        bot.send_sticker(message.chat.id, sti_1)


bot.polling(none_stop=True)
