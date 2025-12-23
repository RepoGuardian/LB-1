import telebot
from telebot import types
import os
from dotenv import load_dotenv

# Завантажуємо змінні оточення
load_dotenv()

# Отримуємо токен з файлу .env
token = os.getenv('BOT_TOKEN')

# Створюємо об'єкт бота
bot = telebot.TeleBot(token)


# Створюємо функцію для обробки команди /start
@bot.message_handler(commands=['start'])
def start(message):
    # Формуємо текст привітання
    text = "Привіт! Я бот для лабораторної роботи.\n\n"
    text += "Доступні команди:\n"
    text += "/menu - показати меню\n"
    text += "/whisper текст - малі літери\n"
    text += "/scream текст - великі літери"

    # Відправляємо повідомлення
    bot.send_message(message.chat.id, text)


# Створюємо функцію для виклику меню
@bot.message_handler(commands=['menu'])
def menu(message):
    # Створюємо клавіатуру
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Додаємо кнопки до клавіатури
    button1 = types.KeyboardButton('Тест whisper')
    button2 = types.KeyboardButton('Тест scream')
    button3 = types.KeyboardButton('Інформація')
    button4 = types.KeyboardButton('Закрити меню')
    keyboard.add(button1, button2)
    keyboard.add(button3)
    keyboard.add(button4)

    # Відправляємо повідомлення з меню
    bot.send_message(message.chat.id, "Меню бота:", reply_markup=keyboard)


# Створюємо функцію для команди whisper
@bot.message_handler(commands=['whisper'])
def whisper(message):
    try:
        # Отримуємо текст повідомлення
        text = message.text.split(' ', 1)[1]

        # Переводимо текст у нижній регістр
        result = text.lower()

        # Відправляємо результат
        bot.reply_to(message, "Результат: " + result)
    except:
        bot.reply_to(message, "Введіть текст після команди")


# Створюємо функцію для команди scream
@bot.message_handler(commands=['scream'])
def scream(message):
    try:
        # Отримуємо текст повідомлення
        text = message.text.split(' ', 1)[1]

        # Переводимо текст у верхній регістр
        result = text.upper()

        # Відправляємо результат
        bot.reply_to(message, "Результат: " + result)
    except:
        bot.reply_to(message, "Введіть текст після команди")


# Обробляємо текстові повідомлення та натискання кнопок
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Тест whisper':
        # Перевіряємо роботу whisper
        test = "ТЕСТОВИЙ ТЕКСТ"
        bot.send_message(message.chat.id, "Було: " + test + "\nСтало: " + test.lower())

    elif message.text == 'Тест scream':
        # Перевіряємо роботу scream
        test = "тестовий текст"
        bot.send_message(message.chat.id, "Було: " + test + "\nСтало: " + test.upper())

    elif message.text == 'Інформація':
        # Відправляємо інформацію про бота
        bot.send_message(message.chat.id, "Це тестовий бот для виконання завдання.")

    elif message.text == 'Закрити меню':
        # Прибираємо клавіатуру
        hide = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, "Меню закрито", reply_markup=hide)

    else:
        # Відповідаємо на невідомий текст
        bot.send_message(message.chat.id, "Я не розумію цього повідомлення.")


# Запускаємо бота
if __name__ == '__main__':
    bot.polling(none_stop=True)