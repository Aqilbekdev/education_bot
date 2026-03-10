from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
storage = MemoryStorage()
dp=Dispatcher(bot,storage=MemoryStorage())

ADMINS = [1491355115]
