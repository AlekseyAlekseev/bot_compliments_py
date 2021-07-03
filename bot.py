from random import randint, choice
from requests import get
from bs4 import BeautifulSoup
from threading import Timer
import telebot

bot = telebot.TeleBot('1862194768:AAEjXPG4ZVpwsgdmjKQ242H2AxosFcmEuFc')


def get_random_compliment():
    random_page_number = str(randint(1, 42))
    webpage = get('http://kompli.me/komplimenty-lyubimoj/page/' +
                  random_page_number).text
    tags = BeautifulSoup(webpage, 'html.parser').find_all('a')
    compliments = []
    for tag in tags:
        tag_text = tag.get_text()
        if tag_text == 'Назад':
            break
        compliments.append(tag_text)

    return choice(compliments[4:])


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот для комплиментов. Приятно познакомиться, {message.from_user.first_name}')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text in ('Привет', 'Хай', 'Ку', 'Приветик',
                        'привет', 'хай', 'ку', 'приветик'
                                               'Привет!', 'Хай!', 'Ку!', 'Приветик!',
                        'привет!', 'хай!', 'ку!', 'приветик!'):
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text in ('Кто тебя создал', 'Кто твой создатель', 'Кто тебя сделал', 'Кто тебя разработал',
                          'кто тебя создал', 'кто твой создатель', 'кто тебя сделал', 'кто тебя разработал',
                          'Кто тебя создал?', 'Кто твой создатель?', 'Кто тебя сделал?', 'Кто тебя разработал?',
                          'кто тебя создал?', 'кто твой создатель?', 'кто тебя сделал?', 'кто тебя разработал?'):
        bot.send_message(message.from_user.id, 'Мой создатель - повелитель мира Алексеев Алексей!')
    elif message.text in ('Как дела', 'Как твои дела', 'Как делишки',
                          'как дела', 'как твои дела', 'как делишки',
                          'как дела?', 'как твои дела?', 'как делишки?',
                          'Как дела?', 'Как твои дела?', 'Как делишки?'):
        bot.send_message(message.from_user.id, 'У меня все хорошо, а как у вас?')
    elif message.text in (
            'Хорошо', 'Прекрасно', 'Замечательно', 'Отлично',
            'хорошо', 'прекрасно', 'замечательно', 'отлично',
            'Хорошо!', 'Прекрасно!', 'Замечательно!', 'Отлично!',
            'хорошо!', 'прекрасно!', 'замечательно!', 'отлично!'):
        bot.send_message(message.from_user.id, 'Рад это слышать!')
    elif message.text in (
            'Плохо', 'Ужасно', 'Не очень', 'Неочень', 'Плачу', 'Грустно',
            'плохо', 'ужасно', 'не очень', 'неочень', 'плачу', 'грустно',
            'Плохо!', 'Ужасно!', 'Не очень!', 'Неочень!', 'Плачу!', 'Грустно!',
            'плохо!', 'ужасно!', 'не очень!', 'неочень!', 'плачу!', 'грустно!'):
        bot.send_message(message.from_user.id, 'Не грустите, вот вам комплиментик:\n')
        bot.callback_query_handler(send_compliment(message))
    elif message.text in ('Можно комплимент?', 'Где мой комплимент?', 'Скажи мне приятное', 'Хочу комплимент',
                          'можно комплимент?', 'где мой комплимент?', 'скажи мне приятное', 'хочу комплимент',
                          'Можно комплимент!', 'Где мой комплимент!', 'Скажи мне приятное!', 'Хочу комплимент!',
                          'можно комплимент!', 'где мой комплимент!', 'скажи мне приятное!', 'хочу комплимент!',
                          'Хочу еще', 'Еще', 'Давай еще',
                          'Хочу еще!', 'Еще!', 'Давай еще!',
                          'хочу еще', 'еще', 'давай еще',
                          'хочу еще!', 'еще!', 'давай еще!',
                          'Хочу ещё', 'Ещё', 'Давай ещё',
                          'Хочу ещё!', 'Ещё!', 'Давай ещё!',
                          'хочу ещё', 'ещё', 'давай ещё',
                          'хочу ещё!', 'ещё!', 'давай ещё!'):
        bot.send_message(message.from_user.id, 'Вот вам комплимент:\n')
        bot.callback_query_handler(send_compliment(message))
    elif message.text in (
            'Спасибо', 'Благодарю', 'спасибо', 'благодарю',
            'Спасибо!', 'Благодарю!', 'спасибо!', 'благодарю!'):
        bot.send_message(message.from_user.id, 'Для Вас все что угодно!')
    else:
        bot.send_message(message.from_user.id, 'Это слишком сложно для меня:(')


def send_compliment_timer():
    Timer(15.0, send_compliment).start()
    bot.send_message(494000679, get_random_compliment())


def send_compliment_timer_Anna():
    Timer(3600.0, send_compliment).start()
    bot.send_message(999489671, get_random_compliment())


def send_compliment(message):
    bot.send_message(message.from_user.id, get_random_compliment())


send_compliment_timer_Anna()
bot.polling()
