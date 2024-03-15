from telegram.ext import Application, CommandHandler
import logging
from telegram import Update
from task_service import service
from config import config


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update, context):
    await update.message.reply_text('Hello! I can fetch Jira issues for you.')

async def get_issues(update, context):
    total_issues = service.get_total_issues_jira()
    await update.message.reply_text(f"Total issues: {total_issues}")

def start_bot():
    app = Application.builder().token(config.TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("getissues", get_issues))
    app.run_polling()

if __name__ == '__main__':
    start_bot()


