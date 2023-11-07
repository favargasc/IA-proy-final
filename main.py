import telebot
from sentiment import Sentiment
from sentiments_analyzer import sentiments_analyzer
from res_regerator import get_res
import csv
import datetime
import matplotlib.pyplot as plt
import pandas as pd

bot = telebot.TeleBot(
    '6304489420:AAFTFInT8mPAlcQyPe5cLL0M-kgdD9Een2M', parse_mode=None)

sentiment = Sentiment()
print("Chatbot is running!")


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hi, how can I help you?")

@bot.message_handler(commands=['graph'])
def send_welcome(message):
    data = pd.read_csv('data.csv')

    data = data.groupby('sentiment').size().reset_index(name='count')

    fig, ax = plt.subplots()
    sentiments = [1, 2, 3, 4, 5]
    labels = ['Muy Triste', 'Triste', 'Neutro', 'Feliz', 'Muy Feliz']
    colors = ['red', 'orange', 'yellow', 'green', 'blue']
    ax.bar(sentiments, data['count'], color=colors)
    ax.set_xticks(sentiments)
    ax.set_xticklabels(labels)
    ax.set_xlabel('Sentimiento')
    ax.set_ylabel('Apariciones')
    ax.set_title('Total de apariciones por sentimiento')
    plt.savefig('graph.jpg')

    with open('graph.jpg', 'rb') as f:
        bot.send_document(message.chat.id, f)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    index = int(sentiments_analyzer(message.text)[0]['label'][0])

    print('Sentiment: ', index)

    current_emoji = "😐"

    if (index == 1):
        current_emoji = "😭"
    elif (index == 2):
        current_emoji = "😔"
    elif (index == 3):
        current_emoji = "😐"
    elif (index == 5):
        current_emoji = "😊"
    else:
        current_emoji = "😃"

    response = get_res(message.text)

    with open("data.csv", "a") as f:
        writer = csv.writer(f, delimiter=",")

        datetime_now = datetime.datetime.now()

        formatted_datetime = datetime_now.strftime("%d-%m-%Y %H:%M:%S")

        writer.writerow([formatted_datetime, index])

    bot.reply_to(message, response + " " + current_emoji)


bot.infinity_polling()
