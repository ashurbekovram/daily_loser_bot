import random
import telegram
from telegram.ext import Updater, CommandHandler

TOKEN = '6142297512:AAFmkmwjDn_gFHJ_ersHX1lVsiKuHxwt80s'
bot = telegram.Bot(token=TOKEN)
chat_id = 'your_chat_id_here'

def pick_random_member(update, context):
    # Получаем список участников группы
    members = bot.get_chat_members_count(chat_id)

    # Выбираем случайного участника
    random_member = random.randint(0, members-1)

    # Получаем информацию о выбранном участнике
    member_info = bot.get_chat_member(chat_id, random_member)

    # Отправляем никнейм выбранного участника в чат
    bot.send_message(chat_id=chat_id, text=member_info.user.username)

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher

dp.add_handler(CommandHandler("pick_random_member", pick_random_member))

updater.start_polling()
updater.idle()
