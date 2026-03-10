from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
keyboard=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📋 Registrations"),
            KeyboardButton(text="📊 Statistika"),
            KeyboardButton(text="📢 Broadcast")
        ],
        [
            KeyboardButton(text="Admin commands")
        ]
    ],resize_keyboard=True
)