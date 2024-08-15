from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import os

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Получите ваш API Token от BotFather
API_TOKEN = os.getenv('API_TOKEN')

# Список диет
DIETS = {
    'low_carb': 'Низкоуглеводная диета - подробное описание...',
    'keto': 'Кето диета - подробное описание...',
    'paleo': 'Палео диета - подробное описание...',
    # Добавьте больше диет по мере необходимости
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Используйте команду /diet <название диеты> для получения информации.')

def diet(update: Update, context: CallbackContext) -> None:
    diet_name = ' '.join(context.args)
    if diet_name in DIETS:
        diet_info = DIETS[diet_name]
        update.message.reply_text(diet_info)
    else:
        update.message.reply_text('Диета не найдена. Используйте команду /start для получения списка команд.')

def main() -> None:
    updater = Updater(API_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('diet', diet))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
