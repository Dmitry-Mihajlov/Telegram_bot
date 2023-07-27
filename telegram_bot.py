import telebot
from telebot import types
from telegram_bot_open import OPEN_NAMES_TASKS, OPEN_CATALOG, OPEN_ANSWER, OPEN_DECISION, OPEN_STIKER, OPEN_PHOTO
from telegram_bot_text import TEXT_START, TEXT_HELP, TEXT_INFO, PROFILE
from telegram_bot_kb_names_tasks import KEYBOARD_NAMES_TASKS
from telegram_bot_kb_guide import KEYBOARD_GUIDE_LINE, KEYBOARD_GUIDE_SQUARE
bot = telebot.TeleBot('5588654975:AAF-vqi_kxwXn49ofthkQcPAw4xfqlP-84s')
user_response = None
user_guide = None
total_try = 0
total_false = 0
solved_tasks = []

@bot.message_handler(commands=['start'])
def start(message):
    """Выводит начальное приветствие и дает команды которые можно использовать"""
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn_1 = types.KeyboardButton(text='/catalog')
    btn_2 = types.KeyboardButton(text='/profile')
    btn_3 = types.KeyboardButton(text='/guide')
    btn_4 = types.KeyboardButton(text='/help')
    btn_5 = types.KeyboardButton(text='ОТВЕТ')
    btn_6 = types.KeyboardButton(text='РЕШЕНИЕ')
    btn_7 = types.KeyboardButton(text='✅')
    btn_8 = types.KeyboardButton(text='❌')
    kb.add(btn_1, btn_2, btn_3, btn_4, btn_5, btn_6, btn_7, btn_8)

    bot.send_message(message.chat.id, TEXT_START(message), reply_markup=kb)


@bot.message_handler(commands=['help'])
def help(message):
    """Выводит просто текст"""
    bot.send_message(message.chat.id, TEXT_HELP(message))

@bot.message_handler(commands=['info'])
def info(message):
    """Выводит просто текст"""
    bot.send_message(message.chat.id, TEXT_INFO(message))

@bot.message_handler(commands=['guide'])
def guide(message):
    """Вывод темы"""
    bot.send_message(message.chat.id, 'Для твоего самостоятельного повторения линейной функции и ее свойств, мы подготовили полезные материалы.', reply_markup=KEYBOARD_GUIDE_LINE(message))
    bot.send_message(message.chat.id, 'А если ты уже отлично знаешь предыдущую тему, тогда скорей начинай повторять квадратичные функции, внизу тебя уже ждут ссылки на полезные ресурсы ☺️', reply_markup=KEYBOARD_GUIDE_SQUARE(message))

@bot.message_handler(commands=['profile'])
def profile(message):
    bot.send_message(message.chat.id, PROFILE(message, solved_tasks, OPEN_CATALOG))



@bot.message_handler(commands=['catalog'])
def names_tasks(message):
    """Выводим названия задач"""
    bot.send_message(message.chat.id, 'Доступные задания:')
    bot.send_message(message.chat.id, ''.join(OPEN_NAMES_TASKS()), reply_markup=KEYBOARD_NAMES_TASKS(message))
    bot.send_message(message.chat.id, 'Если хотите отметить какое то задание решенным, тогда откройте его условие и отправьте ✅, если захотите удалить это задание из списка, то отправьте ❌')

@bot.callback_query_handler(func=lambda callback: callback.data)
def task(callback):
    """Выводим задание"""
    global user_response
    try:
        for i in range(60):
            if callback.data == 'names_tasks: ' + str(i): user_response = i
        bot.send_message(callback.message.chat.id, OPEN_CATALOG()[user_response])
    except:
        print('Произошла ошибка в работе функции task\n'
              f'user_response = {user_response}\n'
              '--------------------------------------------------')

@bot.message_handler(content_types=['text'])
def answer(message):
    """Отправка ответа"""
    global total_try, total_false, solved_tasks
    try:
        if message.text.lower() == 'ответ':
            bot.send_message(message.chat.id, OPEN_ANSWER()[user_response])

        elif message.text.lower() == 'решение':
            bot.send_message(message.chat.id, OPEN_DECISION()[user_response])

        elif message.text == '✅':
            try:
                if total_try == 0 and solved_tasks.count(user_response+1) == 0:
                    bot.send_message(message.chat.id, f'Вы точно хотите отметить задание номер {user_response+1} решенным?\n'
                    'Если да, то отправьте ✅ еще раз для подтверждения')
                    total_try = 1
                elif total_try == 1:
                    bot.send_message(message.chat.id, f'Задание номер {user_response+1} успешно отмечено выполненным')
                    total_try = 0
                    solved_tasks.append(user_response+1)
                else:
                    bot.send_message(message.chat.id, 'Это задание уже отмечено решенным')
            except:
                bot.send_message(message.chat.id, 
                'Упс, что-то не так.\n'
                'Используй интерактивную клавиатуру.\n'
                'Если возникли вопросы, то отправь команду /help или прочитай о возможностях бота на этой версии отправив /info')

        elif message.text == '❌':
            try:
                if total_false == 0 and solved_tasks.count(user_response+1) == 1:
                    bot.send_message(message.chat.id, f'Вы точно хотите удалить номер {user_response+1} из списка решенных?\n'
                    'Если да, то отправьте ❌ еще раз для подтверждения')
                    total_false = 1
                elif total_false == 1:
                    bot.send_message(message.chat.id, f'Задание номер {user_response+1} успешно удалено из списка решенных')
                    total_false = 0
                    solved_tasks.remove(user_response+1)
                else:
                    bot.send_message(message.chat.id, 'Это задание не было отмечено заранее решенным')
            except:
                bot.send_message(message.chat.id, 
                'Упс, что-то не так.\n'
                'Используй интерактивную клавиатуру.\n'
                'Если возникли вопросы, то отправь команду /help или прочитай о возможностях бота на этой версии отправив /info')

        else:
            bot.send_message(message.chat.id, 
            'Упс, что-то не так.\n'
            'Используй интерактивную клавиатуру.\n'
            'Если возникли вопросы, то отправь команду /help или прочитай о возможностях бота на этой версии отправив /info')
    except:
        print('Произошла ошибка в работе функции answer\n' 
              f'user_response = {user_response}\n'
              '--------------------------------------------------')

@bot.message_handler(content_types=['sticker'])
def stiker(message):
    bot.send_sticker(message.chat.id, OPEN_STIKER())


@bot.message_handler(content_types=['photo'])
def photo(message):
    bot.send_sticker(message.chat.id, OPEN_PHOTO())


bot.polling(non_stop=True)