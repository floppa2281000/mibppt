from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "ТУТ_ТВІЙ_TOKEN"

# слова реклами
BAD_WORDS = [
    "http", "https", "t.me", "telegram",
    "заробіток", "casino", "bet", "crypto", "@"
]

async def anti_spam(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    for word in BAD_WORDS:
        if word in text:
            await update.message.delete()
            await update.effective_chat.send_message(
                "Слишком много воды? не правдали?"
            )
            break

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, anti_spam))

app.run_polling()
