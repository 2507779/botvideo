from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import logging
import os

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Получите ваш API Token от BotFather
API_TOKEN = os.getenv('API_TOKEN')

# Категории и видео URL
VIDEO_CATEGORIES = {
    'amateur': ['https://example.com/amateur1.mp4', 'https://example.com/amateur2.mp4'],
    'asian': ['https://example.com/asian1.mp4', 'https://example.com/asian2.mp4'],
    'bikini': ['https://example.com/bikini1.mp4', 'https://example.com/bikini2.mp4'],
    'big_tits': ['https://example.com/big_tits1.mp4', 'https://example.com/big_tits2.mp4'],
    'blowjob': ['https://example.com/blowjob1.mp4', 'https://example.com/blowjob2.mp4'],
    'couples': ['https://example.com/couples1.mp4', 'https://example.com/couples2.mp4'],
    'fisting': ['https://example.com/fisting1.mp4', 'https://example.com/fisting2.mp4'],
    'gangbang': ['https://example.com/gangbang1.mp4', 'https://example.com/gangbang2.mp4'],
    'lesbian': ['https://example.com/lesbian1.mp4', 'https://example.com/lesbian2.mp4'],
    'milf': ['https://example.com/milf1.mp4', 'https://example.com/milf2.mp4'],
    'orgy': ['https://example.com/orgy1.mp4', 'https://example.com/orgy2.mp4'],
    'pornstar': ['https://example.com/pornstar1.mp4', 'https://example.com/pornstar2.mp4'],
    'shaved': ['https://example.com/shaved1.mp4', 'https://example.com/shaved2.mp4'],
    'shemale': ['https://example.com/shemale1.mp4', 'https://example.com/shemale2.mp4'],
    'solo': ['https://example.com/solo1.mp4', 'https://example.com/solo2.mp4'],
    'swallow': ['https://example.com/swallow1.mp4', 'https://example.com/swallow2.mp4'],
    'teen': ['https://example.com/teen1.mp4', 'https://example.com/teen2.mp4'],
    'threesome': ['https://example.com/threesome1.mp4', 'https://example.com/threesome2.mp4'],
    'toys': ['https://example.com/toys1.mp4', 'https://example.com/toys2.mp4'],
    'voyeur': ['https://example.com/voyeur1.mp4', 'https://example.com/voyeur2.mp4'],
    'bukkake': ['https://example.com/bukkake1.mp4', 'https://example.com/bukkake2.mp4'],
    'cuckold': ['https://example.com/cuckold1.mp4', 'https://example.com/cuckold2.mp4'],
    'dirty_talk': ['https://example.com/dirty_talk1.mp4', 'https://example.com/dirty_talk2.mp4'],
    'gfe': ['https://example.com/gfe1.mp4', 'https://example.com/gfe2.mp4'],
    'hairy': ['https://example.com/hairy1.mp4', 'https://example.com/hairy2.mp4'],
    'japanese': ['https://example.com/japanese1.mp4', 'https://example.com/japanese2.mp4'],
    'mature': ['https://example.com/mature1.mp4', 'https://example.com/mature2.mp4'],
    'pov': ['https://example.com/pov1.mp4', 'https://example.com/pov2.mp4'],
    'squirting': ['https://example.com/squirting1.mp4', 'https://example.com/squirting2.mp4'],
    'tattoos': ['https://example.com/tattoos1.mp4', 'https://example.com/tattoos2.mp4'],
    'thighs': ['https://example.com/thighs1.mp4', 'https://example.com/thighs2.mp4'],
    'white_girls': ['https://example.com/white_girls1.mp4', 'https://example.com/white_girls2.mp4'],
    'bbw': ['https://example.com/bbw1.mp4', 'https://example.com/bbw2.mp4'],
    'anal': ['https://example.com/anal1.mp4', 'https://example.com/anal2.mp4'],
    'blonde': ['https://example.com/blonde1.mp4', 'https://example.com/blonde2.mp4'],
}

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Используйте команды /videos <category> для просмотра видео.')

def videos(update: Update, context: CallbackContext) -> None:
    category = ' '.join(context.args)
    if category in VIDEO_CATEGORIES:
        videos = VIDEO_CATEGORIES[category]
        for video in videos:
            context.bot.send_video(chat_id=update.effective_chat.id, video=video)
    else:
        update.message.reply_text('Рубрика не найдена. Используйте команду /start для получения списка команд.')

def main() -> None:
    updater = Updater(API_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('videos', videos))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
