import telebot
bot = telebot.TeleBot('5996138163:AAEAdk88v5qrff5Jn5zVdaHO4z3hZCItUDc')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id,f'Доброе время суток  {message.from_user.last_name} {message.from_user.first_name}')






bot.polling(non_stop=True)