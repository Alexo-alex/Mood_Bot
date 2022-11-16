from telebot import types, TeleBot

# Це наш токен
TOKEN = '5638123036:AAF6qPVKzimeQuBNqpRdbQspuIyjuyP_bcI'

bot = TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    markup_inline = types.ReplyKeyboardMarkup(resize_keyboard=True)
    i_am_roll = types.KeyboardButton(text='Рофл')
    i_am_joyful = types.KeyboardButton(text='Радісний')
    i_am_angry = types.KeyboardButton(text='Агрюсь')
    i_am_norms = types.KeyboardButton(text='Норм')

    markup_inline.add(i_am_roll, i_am_joyful, i_am_angry, i_am_norms)
    bot.send_message(message.chat.id, 'Обери свій муд на сьогодні!', reply_markup=markup_inline)


@bot.message_handler(content_types=['text'])
def get_text(message):
    print(message.text)
    if message.text == 'Рофл':
        sti_1 = open('static/Laughs_to_tears.png', 'rb')
        bot.send_sticker(message.chat.id, sti_1)
    elif message.text == 'Радісний':
        sti_1 = open('static/Cheerful.png', 'rb')
        bot.send_sticker(message.chat.id, sti_1)
    elif message.text == 'Агрюсь':
        sti_1 = open('static/Angry.png', 'rb')
        bot.send_sticker(message.chat.id, sti_1)
    elif message.text == 'Норм':
        sti_1 = open('static/Poker_face.png', 'rb')
        bot.send_sticker(message.chat.id, sti_1)


bot.polling(none_stop=True)
