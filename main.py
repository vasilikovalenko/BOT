import random
import telebot
import webbrowser
from telebot import types



# Передаем сюда токен, который получили от FatherBot
bot = telebot.TeleBot('5996138163:AAEAdk88v5qrff5Jn5zVdaHO4z3hZCItUDc')
# Варианты ответов пользователю, если тот ввел непонятное боту сообщение
answers = ['Я не понял, что ты хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды.', 'Мой разработчик не говорил, что отвечать в такой ситуации... >_<']

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # Добавляем кнопки, которые будут появляться после ввода команды /start
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Меню')
    
    # Разделяю кнопки по строкам так, чтобы товары были отдельно от остальных кнопок
    markup.row(button1)
    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nУ меня ты сможешь купить некоторые товары!\nКонтакт моего разработчика:ссылка ...', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)

# Обработка фото. Если пользователь пришлет фото, то бот отреагирует на него. Можно реализовать свой функционал
@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')

# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == 'Меню':
        goodsChapter(message)
    elif message.text == '4 сезона':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('4 sezona.jpeg','rb')
        bot.send_photo(message.chat.id,file, 'Информация  4 сезона', reply_markup=markup)
    elif message.text == '4 сыра':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('4sira.jpg','rb')
        bot.send_photo(message.chat.id, file,'Информация 4 сыра', reply_markup=markup)
    elif message.text == 'Cицилийская':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('siziliiskaia.jpg','rb')
        bot.send_photo(message.chat.id,file,'Информация сицилийская', reply_markup=markup)
    elif message.text == 'Гавайская':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('gava.jpg','rb')
        bot.send_photo(message.chat.id, file,'Информация гавайская', reply_markup=markup)
    elif message.text == 'Вегетарианская':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('veget.jpg','rb')
        bot.send_photo(message.chat.id,file,'Информация Вегетарианская', reply_markup=markup) 
    elif message.text == 'Моргаритта':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open("morgarita.jpg",'rb')
        bot.send_photo(message.chat.id,file, 'Информация Моргаритта', reply_markup=markup) 
    elif message.text == 'Мясная':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('mias.jpg','rb')
        bot.send_photo(message.chat.id,file,'Информация мясная', reply_markup=markup) 
    elif message.text == 'Капричеза':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('kaprichioza.jpg','rb')
        bot.send_photo(message.chat.id,file, 'Информация капричеза', reply_markup=markup)  
    elif message.text == 'Фокачча':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('foka.jpeg','rb')
        bot.send_photo(message.chat.id,file, 'Информация фокачча', reply_markup=markup)   
    elif message.text == 'Цезарь':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('zezar.jpg','rb')
        bot.send_photo(message.chat.id,file, 'Информация цезарь', reply_markup=markup) 
    elif message.text == 'Морская':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 cделать заказ')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        file=open('mors.jpg','rb')
        bot.send_photo(message.chat.id,file, 'Информация морская', reply_markup=markup)          
    elif message.text == '💳 зделать заказ' or message.text == ' Написать разработчику':
        webbrowser.open( 'id:5047586041')
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню%':
        welcome(message)
    # Если пользователь написал свое сообщение, то бот рандомно генерирует один из возможных вариантов ответа
    # Добавлять и редактировать варианты ответов можно в списке answers
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])

# Функция, отвечающая за раздел товаров
def goodsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('4 сезона')
    button2 = types.KeyboardButton('4 сыра')
    button3 = types.KeyboardButton('Cицилийская')
    button4 = types.KeyboardButton('Гавайская')
    button4 = types.KeyboardButton('Вегетарианская')
    button5 = types.KeyboardButton('Моргаритта')
    button6 = types.KeyboardButton('Мясная')
    button7 = types.KeyboardButton('Капричеза')
    button8 = types.KeyboardButton('Фокачча')
    button9 = types.KeyboardButton('Цезарь')
    button10= types.KeyboardButton('Морская ')
    button11=types.KeyboardButton('Гавайская')
    button12=types.KeyboardButton('↩️ Назад в меню%')
    markup.row(button1,button2,button3,button4,button5)
    markup.row(button6,button7,button8,button9,button10)
    markup.row(button11,button12)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)






bot.polling(none_stop=True)