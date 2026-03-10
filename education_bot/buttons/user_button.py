from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup,InlineKeyboardButton

user_kb=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📚 Kurslar dizimi"),
        ],
        [
            KeyboardButton("📍 Manzil"),
            KeyboardButton("ℹ️ Biz haqqimizda"),
            KeyboardButton("Admin")
        ]
    ],
    resize_keyboard=True
)

kurslar=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Data science",callback_data="data_science"),
            InlineKeyboardButton(text="Python-backend",callback_data="python_backend"),

        ],
        [
            InlineKeyboardButton(text="Frontend",callback_data="frontend"),
            InlineKeyboardButton(text="Grafik dizayn",callback_data="grafik_dizayn")
        ],
        [
            InlineKeyboardButton(text="Onlayn kurslar",callback_data="onlayn_kurs")
        ],
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data="back_main")
        ]
    ],
)

python_kurs=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursqa jaziliw",callback_data="register_python")
        ],
        [
            InlineKeyboardButton(text="Dawamliligi",callback_data="p_dawamliligi"),
            InlineKeyboardButton(text="Kurs bahasi",callback_data="p_bahasi")
        ],
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data='back_kurs')
        ]
    ]
)

frontend_kurs=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursqa jaziliw",callback_data="register_frontend")
        ],
        [
            InlineKeyboardButton(text="Dawamliligi",callback_data="f_dawamliligi"),
            InlineKeyboardButton(text="Kurs bahasi",callback_data="f_bahasi")
        ],
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data='back_kurs')
        ]
    ]
)
science_kurs=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursqa jaziliw",callback_data="register_data_science")
        ],
        [
            InlineKeyboardButton(text="Dawamliligi",callback_data="d_dawamliligi"),
            InlineKeyboardButton(text="Kurs bahasi",callback_data="d_bahasi")
        ],
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data='back_kurs')
        ]
    ]
)
grafik_kurs=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursqa jaziliw",callback_data="register_grafik_dizayn")
        ],
        [
            InlineKeyboardButton(text="Dawamliligi",callback_data="g_dawamliligi"),
            InlineKeyboardButton(text="Kurs bahasi",callback_data="g_bahasi")
        ],
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data='back_kurs')
        ]
    ]
)
back_python=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data='python_back')
        ]
    ]
)
back_data=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data='data_back')
        ]
    ]
)
back_frontend=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data='frontend_back')
        ]
    ]
)
back_grafik=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data='grafik_back')
        ]
    ]
)
onlayn_kurs=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kompyuter sawatxanligi🖥️",callback_data='kompyuter'),
            InlineKeyboardButton(text="IT Foundation🧑‍💻",callback_data="foundation")
        ],
        [
            InlineKeyboardButton(text="⬅️Artqa",callback_data="back_main")
        ]]
)
kompyuter_kurs=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursdi satip aliw",callback_data="komp_aliw")
        ],
        [
            InlineKeyboardButton(text="Demo sabaqdi koriw",callback_data="komp_demo"),
            InlineKeyboardButton(text="⬅️Artqa",callback_data="komp_back")
        ]
    ]
)
foundation_kurs=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Kursdi satip aliw",callback_data="foun_aliw")
        ],
        [
            InlineKeyboardButton(text="Demo sabaqdi koriw",callback_data="foun_demo"),
            InlineKeyboardButton(text="⬅️Artqa",callback_data="foun_back")
        ]
    ]
)
komp_demo=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-sabaq"),
            KeyboardButton(text="4-sabaq"),
        ],
        [
            KeyboardButton("12-sabaq"),
            KeyboardButton("Kompyuter kursqa qaytiw")
        ]
    ],resize_keyboard=True)
foun_demo=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="1-demo sabaq"),
            KeyboardButton(text="2-demo sabaq"),
        ],
        [
            KeyboardButton("3-demo sabaq"),
            KeyboardButton("Foundation kursqa qaytiw")
        ]
    ],
    resize_keyboard=True)

admin_lichka = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Admin menen baylanisiw",url="https://t.me/aqilbekseylbekov")
        ]
    ]
)

onlayn_sabaq=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Link arqali kanalga otin",url="https://https://t.me/saudabdulwahed")
        ]
    ]
)


