from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "8372718905:AAGLga3cB9E3WKFjdDZGG_xCnz8s9-5wt_A"

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
