import re
from aiogram.types import CallbackQuery, Message
from aiogram.dispatcher import FSMContext, Dispatcher
from education_bot.loader import ADMINS, bot
from education_bot.database.create_db import add_registration, check_duplicate
from education_bot.states.register_state import RegisterState


def register_register_handlers(dp: Dispatcher):
    # ---------- COURSE SELECT ----------
    @dp.callback_query_handler(lambda c: c.data.startswith("register_"), state="*")
    async def register_course(callback: CallbackQuery, state: FSMContext):
        await callback.answer()

        raw_course = callback.data.replace("register_", "", 1)
        course_name = raw_course.replace("_", " ").title()

        await state.update_data(course=course_name)
        await callback.message.answer(
            f"📚 {course_name} kursi tanlandi.\n📛 Toliq atinizdi jazin (Maselen: Aqilbek):")
        await RegisterState.full_name.set()

    @dp.message_handler(state=RegisterState.full_name)
    async def get_full_name(message: Message, state: FSMContext):
        full_name = message.text.strip()

        if not re.match(r"^[a-zA-Z‘ʼ’'` ]+$", full_name) or len(full_name) < 5:
            await message.answer("⚠️ Iltimas, ati ham familiyanizdi toliq ham tek hariplerden paydalanip jazin jazin!")
            return

        await state.update_data(full_name=full_name)
        await message.answer("📞 Telefon nomerinizdi jiberin:\n*(Maselen: +998901234567)*")
        await RegisterState.phone.set()

    # ---------- PHONE VALIDATION ----------
    @dp.message_handler(state=RegisterState.phone)
    async def get_phone(message: Message, state: FSMContext):
        phone = message.text.strip().replace(" ", "")  # Bo'shliqlarni olib tashlaymiz

        phone_pattern = r"^(\+?998)?(90|91|93|94|95|97|98|99|33|88|77)\d{7}$"
        if not re.match(phone_pattern, phone):
            await message.answer("⚠️ Telefon nomer formati naduris!\nMisal: +998901234567")
            return

        data = await state.get_data()
        course = data.get("course")
        full_name = data.get("full_name")

        if check_duplicate(message.from_user.id):
            await message.answer("⚠️ Siz Aldin dizimnen o‘tgensiz!")
            await state.finish()
            return

        add_registration(
            user_id=message.from_user.id,
            course=course,
            full_name=full_name,
            phone=phone
        )

        await state.finish()
        await message.answer(
            f"✅ Dizimnen otiw qabil qilindi!\n\n📚 Kurs: {course}\n👤 Ati: {full_name}\n📞 Tel: {phone}")

        admin_msg = f"🆕 Taza oqiwshi:\n📚 Kurs: {course}\n👤 Ati: {full_name}\n📞 Tel: {phone}"
        for admin_id in ADMINS:
            try:
                await bot.send_message(admin_id, admin_msg)
            except:
                pass