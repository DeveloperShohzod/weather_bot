import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from settings import *

updater = Updater(token=TEELEGRAM_TOKEN, use_context=True)



def start(update: Update, context: CallbackContext):
    update.message.reply_text("Ob-havo botiga hush kelibsiz!!\n"
                              "So'rovingizni /search komandasidan keyin kiriting!!!")


def search(update: Update, context: CallbackContext):
    word = context.args
    manzil = ' '.join(word)

    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    querystring = {"q": f"{manzil}", "days": "1"}

    headers = {
        "X-RapidAPI-Key": "b7254b36bdmshda5c6a8da405d6bp1badaejsnc7826b919cc7",
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    xabar = response.json()

    update.message.reply_text(
        f"Joylashuv:{xabar['location']['region']} \n Xarorat:{xabar['current']['temp_c']} C \n "
        f"Shamol tezligi:{xabar['current']['wind_mph']} m/s \n Havo holati:{xabar['current']['condition']['text']} ")


dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('search', search))
updater.start_polling()
updater.idle()
