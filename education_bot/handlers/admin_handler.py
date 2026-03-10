from education_bot.loader import ADMINS,bot
from aiogram import types
from aiogram.dispatcher import Dispatcher
from education_bot.buttons.admin_button import keyboard
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

class BroadcastState(StatesGroup):
    waiting_for_message = State()

import sqlite3

DB_NAME = "education.db"


def register_admin_handlers(dp: Dispatcher):

    @dp.message_handler(commands=["admin"], state="*")
    async def admin_panel(message: types.Message):
        if message.from_user.id not in ADMINS:
            return await message.answer("❌ Siz admin emessiz.")

        await message.answer("🛠 Admin Panel", reply_markup=keyboard)

    @dp.message_handler(lambda message: message.text == "📋 Registrations")
    async def show_registrations(message: types.Message):
        if message.from_user.id not in ADMINS:
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT full_name, phone, course FROM registrations")
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            return await message.answer("❌ Ele esh kim jazilmagan.")

        text = "📋 Dizimnen o‘tgenler:\n\n"
        for row in rows:
            text += f"👤 {row[0]}\n📞 {row[1]}\n📚 {row[2]}\n\n"



        await message.answer(text)

    @dp.message_handler(lambda message: message.text == "📊 Statistika")
    async def statistics(message: types.Message):
        if message.from_user.id not in ADMINS:
            return

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM registrations")
        total = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM registrations
            WHERE DATE(created_at) = DATE('now')
        """)
        today = cursor.fetchone()[0]

        cursor.execute("""
            SELECT COUNT(*) FROM registrations
            WHERE created_at >= DATE('now', '-7 day')
        """)
        week = cursor.fetchone()[0]

        cursor.execute("""
            SELECT course, COUNT(*) as cnt
            FROM registrations
            GROUP BY course
            ORDER BY cnt DESC
        """)
        courses = cursor.fetchall()
        conn.close()

        text = "📊 <b>BOT STATISTIKASI</b>\n\n"
        text += f"👥 Jami registratsiya: <b>{total}</b>\n"
        text += f"📅 Bugin qosilgan: <b>{today}</b>\n"
        text += f"📈 Aqirgi 7 kun: <b>{week}</b>\n\n"

        text += "📚 <b>Kurslar boyinsha:</b>\n"

        most_popular = None

        for course in courses:
            text += f"• {course[0]} — {course[1]} ta\n"
            if not most_popular:
                most_popular = course[0]

        if most_popular:
            text += f"\n🏆 Eng tiykargi kurs: <b>{most_popular}</b>"

        await message.answer(text, parse_mode="HTML")
    @dp.message_handler(lambda message: message.text == "📢 Broadcast")
    async def start_broadcast(message: types.Message):
        if message.from_user.id not in ADMINS:
            return

        await message.answer("✍️ Jibermekshi bolgan xabarinizdi jazin:")
        await BroadcastState.waiting_for_message.set()

    @dp.message_handler(commands=["send"])
    async def send_to_one_user(message: types.Message):

        if message.from_user.id not in ADMINS:
            return

        try:
            args = message.text.split(maxsplit=2)
            user_id = int(args[1])
            text = args[2]

            await bot.send_message(user_id, text)
            await message.answer("✅ Xabar jiberildi!")


        except ValueError:
            await message.answer("❌ Format qate.\nMisali:\n/send 123456789 Salem")

    @dp.message_handler(commands=["delete"])
    async def delete_user(message: types.Message):

        if message.from_user.id not in ADMINS:
            return

        args = message.get_args()

        if not args:
            return await message.answer("❌ Format:\n/delete 123456789")

        try:
            user_id = int(args)

            conn = sqlite3.connect(DB_NAME)
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM registrations WHERE user_id = ?", (user_id,))
            user = cursor.fetchone()

            if not user:
                await message.answer("❌ Bunday user topilmadi.")
                conn.close()
                return

            cursor.execute("DELETE FROM registrations WHERE user_id = ?", (user_id,))
            conn.commit()

            await message.answer("✅ User muvaffaqiyatli o‘chirildi.")

            conn.close()

        except ValueError:
            await message.answer("❌ ID faqat raqam bo‘lishi kerak.")
        except Exception as e:
            await message.answer(f"❌ Xatolik: {e}")

    @dp.message_handler(text="Admin commands")
    async def admin_command(message: types.Message):
        await message.answer("""
        Admin ushin commandlar dizimi
        /delete user_id
        /send user_id sms
        """)


    @dp.message_handler(state=BroadcastState.waiting_for_message)
    async def send_broadcast(message: types.Message, state: FSMContext):

        if message.from_user.id not in ADMINS:
            return

        broadcast_text = message.text

        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()

        cursor.execute("SELECT DISTINCT user_id FROM registrations")
        users = cursor.fetchall()

        conn.close()

        success = 0
        failed = 0

        for user in users:
            try:
                await message.bot.send_message(user[0], broadcast_text)
                success += 1
            except ValueError:
                failed += 1

        await message.answer(
            f"✅ Broadcast juwmaqlandi!\n\n"
            f"📤 Jiberildi: {success}\n"
            f"❌ Qatelik: {failed}"
        )

        await state.finish()
