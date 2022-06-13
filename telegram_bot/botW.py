import logging
from flask import Flask,request
from telegram.ext import Updater, CommandHandler,MessageHandler,Filters,Dispatcher
from telegram import Bot,Update
from util import get_reply

logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN="5502827739:AAGrXF8x1tmNSmrKOcDMBdBvS19D5FvFSvo"

app=Flask(__name__)  #flask app object
@app.route('/')
def index():
    return "Hello !"

@app.route(f'/{TOKEN}', methods=[ 'GET','POST'])
def webhook():
    #create update object from json.format request data
    update=Update.de_json(request.get_json(),bot)
    #process update
    dp.process_update(update)
    return "ok"

def start(bot,update):
        author=update.message.from_user.first_name
        reply="HI,Welcome back {}".format(author)
        bot.sendMessage(chat_id=update.message.chat_id,text=reply)
   
def help(update,context):
    help_txt="Hey! This is help text."
    context.bot.sendMessage(chat_id=update.message.chat_id,text=help_txt)

def reply_text(update,context): #chnge hua h 
   # reply=update.message.text
    intent,reply=get_reply(update.message.text,update.message.chat_id)
    #context.bot.sendMessage(chat_id=update.message.chat_id,text=reply)
    if intent == "get_news":
        reply_text='OK! got it I will show you news with {}'.format(reply)
        context.bot.sendMessage(chat_id=update.message.chat_id,text=reply_text)
    else:
        context.bot.sendMessage(chat_id=update.message.chat_id,text=reply)

def error(update,context):
    logger.error("Update '%s caused error '%s'",update,update.error)


def echo_stickers(update,context):
    context.bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)
    

if __name__== "__main__":
    bot=Bot(TOKEN)
    bot.set_webhook("https://618e-103-214-118-103.in.ngrok.io/ "+TOKEN)
    
    dp=Dispatcher(bot,None)

    dp.add_handler(CommandHandler("start", start)) 
    dp.add_handler(CommandHandler("help", help)) 
    dp.add_handler(MessageHandler(Filters.text, reply_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_stickers)) 
    dp.add_error_handler(error) 
    app.run(port=8443)
   


