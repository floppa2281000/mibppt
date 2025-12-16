import os
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("BOT_TOKEN")  # ← токен НЕ тут

MEME_REPLIES = [
    "Ох сколько много воды в одном тексте... не надоело?~"
]

BAD_WORDS = [
    "http", "https", "t.me", "telegram",
    "crypto", "casino", "bet", "заробіток"
]

import random

async def anti_spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message or not update.message.text:
        return

    text = update.message.text.lower()

    for word in BAD_WORDS:
        if word in text:
            await update.message.delete()
            await update.effective_chat.send_message(
                random.choice(MEME_REPLIES)
            )
            break

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anti_spam))

print("ага")
app.run_polling()
