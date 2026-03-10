from aiogram import executor
from education_bot.loader import dp

from education_bot.handlers.user_handler import register_user_handlers
from education_bot.handlers.register_handler import register_register_handlers
from education_bot.handlers.admin_handler import register_admin_handlers
import database.create_db as db

db.create_db()

register_user_handlers(dp)
register_register_handlers(dp)
register_admin_handlers(dp)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)