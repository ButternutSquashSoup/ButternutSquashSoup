from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Set your own generic message here
generic_message = "Hello! This is a generic message set by the bot owner."

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(generic_message)

def main() -> None:
    # Replace 'YOUR_TOKEN' with your own Telegram bot token
    updater = Updater("YOUR_TOKEN")
    
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
