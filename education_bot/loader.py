from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
bot = Bot(token="7874184131:AAEhXCgLj9KMlaqzFsCQ4KTuMFDyk_MjEA8", parse_mode="HTML")
storage = MemoryStorage()
dp=Dispatcher(bot,storage=MemoryStorage())

ADMINS = [1491355115]
