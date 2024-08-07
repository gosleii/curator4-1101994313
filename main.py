import telebot

bot = telebot.TeleBot("7438178573:AAHxqahjbVWYlx5C_3ZeLGtCj1jMTJPyg14")


@bot.message_handler(command=["start"])
def start_handler(message):
    bot.send_message(message.chat.id, "Приветствую. Что хотите узнать?")


@bot.message_handler(command=["information"])
def start_handler(message):
    bot.send_message(message.chat.id,
                     "Этот бот был создан ради выполнения домашнего задания по бесплатному вебинарию команды **Умскул**")


@bot.message_handler(command=["evaluation"])
def start_handler(message):
    bot.send_message(message.chat.id,
                     "Достаточно комфортный урок, благодаря которому мой кожаный создатель сумел научиться хоть чему-то и будет дальше развиваться в направлении программирования")


@bot.message_handler(command=["gratitude"])
def start_handler(message):
    bot.send_message(message.chat.id,
                     "Мой разработчик благодарен команде Умскул за такую возможность безвозмездно научиться такой востребованной в наше время деятельности. Спасибо вам!")


bot.infinity_polling()