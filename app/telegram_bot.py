import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram import InlineKeyboardMarkup, InlineKeyboardButton

from task_service import service
from config import config

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

keyboard_buttons = [
    [InlineKeyboardButton('Fetch Jira Issues', callback_data='fetch_issues')],
    [InlineKeyboardButton('Help', callback_data='help_command')],
]

keyboard = InlineKeyboardMarkup(keyboard_buttons)

async def handle_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Choose an action:', reply_markup=keyboard)  # type: ignore

async def fetch_issues(update: Update, context):
    total_issues = service.get_total_issues_jira()
    await update.callback_query.edit_message_text(f"Total issues: {total_issues}", reply_markup=keyboard)  # type: ignore
    await update.callback_query.answer('Issues fetched successfully.')  # type: ignore

async def help_command(update: Update, context):
    await update.callback_query.edit_message_text(f"Use `/start` to fetch Jira issues.", reply_markup=keyboard)  # type: ignore
    await update.callback_query.answer('Help command successfully.')  # type: ignore



def start_bot():
    app = Application.builder().token(config.TELEGRAM_TOKEN).build()

    app.add_handler(CommandHandler('start', handle_keyboard))
    app.add_handler(CallbackQueryHandler(fetch_issues, pattern='fetch_issues'))
    app.add_handler(CallbackQueryHandler(help_command, pattern='help_command'))

    try:
        app.run_polling()
    except Exception as e:
        logging.error(f'An error occurred: {e}')
    else:
        logging.info('Bot stopped.')

if __name__ == '__main__':
    start_bot()