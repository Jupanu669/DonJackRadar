import telegram
import time

BOT_TOKEN = '7592661384:AAFu_heh6pLBEhX3pOOB4w0UlbX3sb36LgY'
CHANNEL_ID = '-1002871227749'

bot = telegram.Bot(token=BOT_TOKEN)

def send_start_message():
    message = """
🏴‍☠️ DonJack Radar ONLINE 🧭

Botul a acostat în portul Corabia Matelotilor.  
Începem vânătoarea de tokenuri! 🚀
"""
    bot.send_message(chat_id=CHANNEL_ID, text=message)

if __name__ == "__main__":
    while True:
        send_start_message()
        time.sleep(3600)  # trimite un mesaj la fiecare oră
