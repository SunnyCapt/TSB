import logging

from bot import data
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async

logging.basicConfig(level=logging.INFO)

books = data.books


def search(_text):
    result = []
    _text = data.clear(_text)
    for author in books.keys():
        for book in books[author].keys():
            if books[author][book].find(_text) != -1:
                result.append({"message": "", "author": author, "book": book})
    if len(result) == 0: result.append({"message": "Не нашел, прости...", "author": "", "book": ""})
    return result


@run_async
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text='Пришли мне цитату, а я попытаюсь ее найти')


@run_async
def text(bot, update):
    _text = update.message.text
    try:
        bot.sendMessage(chat_id=update.message.chat_id, text='Поиск...')
        result = search(_text)
        bot.sendMessage(chat_id=update.message.chat_id,
                        text="".join(["%s\n<strong>%s</strong>\n<code>%s</code>\n==================" % (
                            val["message"], val["author"], val["book"]) for val in result]), parse_mode="HTML")
    except:
        print("dont work :(")


updater = Updater(token=data.bot_token)  # , request_kwargs={'proxy_url':"protocol://host:port"} )
start_handler = CommandHandler('start', start)
text_handler = MessageHandler(Filters.text, text)
updater.dispatcher.add_handler(start_handler)
updater.dispatcher.add_handler(text_handler)
updater.start_polling()
updater.idle()
