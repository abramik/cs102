import requests
import config
import telebot
from bs4 import BeautifulSoup
from typing import List, Tuple

access_token = '1059996494:AAHhNEyAqoJD1KV9HWC96jnE3hux83qrDvM'
proxy = {'https': 'https://23.237.22.172:3128'}

# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(content_types=['text'])
def echo(message: str) -> None:
    bot.send_message(message.chat.id, message.text)


day_list = ['monday',  'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
day_rus = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']


def get_page(group: str, week: str='') -> str:
    if week:
        week = str(week) + '/'
    url = f'{config.domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'
    response = requests.get(url)
    web_page = response.text
    return web_page


if __name__ == '__main__':
    bot.polling()
