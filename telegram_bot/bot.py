import logging
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters

logging.basicConfig(format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN="5502827739:AAGrXF8x1tmNSmrKOcDMBdBvS19D5FvFSvo"

def start(update,context):
        author=update.message.from_user.first_name
        reply="HI,Welcome back {}".format(author)
        context.bot.sendMessage(chat_id=update.message.chat_id,text=reply)
   
def help(update,context):
    help_txt="Hey! This is help text."
    context.bot.sendMessage(chat_id=update.message.chat_id,text=help_txt)

def echo_text(update,context):
    reply=update.message.text
    context.bot.sendMessage(chat_id=update.message.chat_id,text=reply)

def error(update,context):
    logger.error("Update '%s caused error '%s'",update,update.error)


def echo_stickers(update,context):
    context.bot.send_sticker(chat_id=update.message.chat_id,sticker=update.message.sticker.file_id)


def  main():
    updater=Updater(TOKEN)
    dp=updater.dispatcher

    dp.add_handler(CommandHandler("start", start)) 
    dp.add_handler(CommandHandler("help", help)) 
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_stickers)) 
    dp.add_error_handler(error) 
    print("......")
    updater.start_polling()  
    logger.info("Started Polling.....")
    updater.idle()

if __name__== "__main__":
    main()
   


