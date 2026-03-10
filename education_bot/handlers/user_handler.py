from aiogram import types
from aiogram.types import Message,CallbackQuery
from aiogram.dispatcher import Dispatcher
from education_bot.buttons.user_button import *
from education_bot.loader import bot
from aiogram.types import LabeledPrice

CLICK_TOKEN = "398062629:TEST:999999999_F91D8F69C042267444B74CC0B3C747757EB0E065"


def register_user_handlers(dp: Dispatcher):
    @dp.message_handler(commands=["start"],state='*')
    async def start_handler(message: types.Message):
        # await state.finish()
        await message.answer(
            "👋 Assalawma aleykum!\n\n"
            "🚀 Bizdin IT Academy botimizga xosh kelipsiz!\n"
            "📚 Zamanagoy IT kasiplerin professionallar menen uyrenin.\n\n"
            "Tomendegi menyudan kerekli bolimdi saylan ⬇️",
            reply_markup=user_kb
        )
    @dp.message_handler(text="📚 Kurslar dizimi")
    async def kurslar_handler(message: Message):
        await message.answer(
            "💡 Biz sizge zamanagoy IT jonelisler boyinsha kurslardi usinis qilamiz!\n\n"
            "👨‍💻 Ameliy joybarlarga tiykarlangan talim\n"
            "🎓 Professional mentorlar\n"
            "🚀 Jumisqa kiriwde jardem\n\n"
            "Tomendegi kurslardan birin saylan ⬇️",
            reply_markup=kurslar
        )
    @dp.message_handler(text='📍 Manzil')
    async def manzil_handler(message: Message):
        await message.answer("Bul bizdin manzilimiz!\n"
                             "🏢Nokis qalasi IT-park 5-etaj\n"
                             "☎️Baylanis ushin nomer:+998944679949")
        await bot.send_location(chat_id=message.from_user.id, latitude=42.458661673815854,longitude=59.61209056929872)

    @dp.message_handler(text="Admin")
    async def admin_lich(message:Message):
        await message.answer("Admin menen baylanisiw ushin tomendegi knopkani basin!",
                             reply_markup=admin_lichka)

    @dp.message_handler(text="ℹ️ Biz haqqimizda")
    async def info_handler(message: types.Message):
        await message.answer("Biz - zamanagóy IT kásiplerdi úyretetuǵın professional akademiya.\n"
                             "✅ Sapalı bilimlendiriw\n"
                             "👨‍💻Ámeliy joybarlar\n"
                             "🤝 Tájiriybeli mentorlar\n"
                             "🚀 Jumısqa jaylasıwda járdem\n"
                             "Biz benen keleshek kásibińizdi házirden baslań!")

    @dp.callback_query_handler(text="python_backend")
    async def python_info(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer_photo(
            photo="AgACAgIAAxkBAAIB82mcjO0GEvBVUSXbacOzONec2zHrAAJHGmsbwkrgSDl32tvwvSqyAQADAgADeAADOgQ",
        caption="""
    <b>🐍 Python Backend Development</b>

    🔹 Python dasturlew tiykarlari  
    🔹 Django / FastAPI frameworklar  
    🔹 Database menen islew (PostgreSQL, MySQL)  
    🔹 API jaratiw texnologiyalari  
    🔹 Real joybarlar ustinde islesiw  

    🚀 Kurs dawaminda siz junior backend developer bolip shigiwiniz mumkin!
    """,reply_markup=python_kurs)

    @dp.callback_query_handler(text="frontend")
    async def frontend_info(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer_photo(
            photo="AgACAgIAAxkBAAIB8GmcjOHKmHrI7X03Q0vBr3__s-PzAAJGGmsbwkrgSIAfCj_Sc4q0AQADAgADeAADOgQ",
        caption="""
    <b>💻 Frontend Development</b>

    ✨ HTML, CSS, JavaScript tiykarlari  
    ⚡ React.js framework  
    🎨 Responsive UI design  
    📱 Web sayt interfeyslarin jaratiw  
    🧠 Real project practice  

    🚀 Zamanagoy web texnologiyalarin professional darajede uyrenin!
    """,reply_markup=frontend_kurs)

    @dp.callback_query_handler(text="grafik_dizayn")
    async def grafik_info(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer_photo(
            photo="AgACAgIAAxkBAAIB6mmcjNZkHxqRNjIpBPXwK1ENuQXEAAJEGmsbwkrgSL1gBegv76ooAQADAgADbQADOgQ",
        caption="""
    <b>🎨 Grafik Dizayn</b>

    🖌 Logo design  
    📱 Social media post design  
    🎭 Branding tiykarlari  
    ✨ Photoshop ham Figma menen islew  
    💡 Kreativ pikirlew texnikalari  

    🚀 Professional dizayner bolip baslan!
    """,reply_markup=grafik_kurs)

    @dp.callback_query_handler(text="data_science")
    async def data_info(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer_photo(
            photo="AgACAgIAAxkBAAIB7WmcjNtQeP28oD2cCPxvwj7WWtvNAAJFGmsbwkrgSJtOxu_Zn03RAQADAgADbQADOgQ",
        caption="""
    <b>📊 Data Science</b>

    📈 Python menen data analiz  
    🤖 Machine Learning tiykarlari  
    📉 Statistik model quriw  
    🧠 AI texnologiyalar  
    🔬 Real datasetlar menen islew  

    🚀 Kelejek kasiplerin birin hazirden uyrenin!
    """,reply_markup=science_kurs)

    @dp.callback_query_handler(text="back_kurs")
    async def back_kurs(call:CallbackQuery):
        await call.message.delete()
        await call.message.answer("Biz sizge to'mendegishe IT kurslardi usinamiz⬇️",reply_markup=kurslar)

    @dp.callback_query_handler(text="back_main")
    async def back_handler(call: CallbackQuery):
        await call.message.delete()

        await call.message.answer(
            "Botga xush kelibsiz!",
            reply_markup=user_kb
        )
    @dp.callback_query_handler(text="p_dawamliligi")
    async def python_d(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("""
        <b>🐍 Python Backend Development</b>

        📅 Kurs dawamliligi: <b>6 ay</b>  
        📆 Haptede: <b>3 kun</b>  
        ⏰ Sabaq waqti: <b>18:00 – 20:00</b>  

        📖 <b>1-ay</b> — Python tiykarlari  
        🔹 Variable, loop, function  
        🔹 OOP tusinigi  

        📖 <b>2-ay</b> — Backend framework  
        🔹 Django / FastAPI  
        🔹 API jaratiw  

        📖 <b>3-4-ay</b> — Database  
        🔹 PostgreSQL / MySQL  
        🔹 CRUD system  

        📖 <b>5-6-oy</b> — Real joybar  
        🔹 Portfolio project  

        ⭐ Kurs aqirinda <b>Junior Backend Developer</b> boliw imkaniyati!
        """,reply_markup=back_python)
    @dp.callback_query_handler(text="f_dawamliligi")
    async def frontend_d(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("""
                <b>💻 Frontend Development</b>
        
                📅 Kurs dawamliligi: <b>5 ay</b>  
                📆 Haptede: <b>3 kun</b>  
                ⏰ Sabaq waqti: <b>18:00 – 20:00</b>  
        
                📖 <b>1-ay</b> — HTML, CSS tiykarlari  
                📖 <b>2-ay</b> — JavaScript tiykarlari  
                📖 <b>3-ay</b> — React.js framework  
                📖 <b>4-5-ay</b> — Real web project  
        
                🎨 Responsive UI design  
                🚀 Portfolio jaratiw
        
                ⭐ Junior Frontend Developer boliw imkaniyati!
                """,reply_markup=back_frontend)

    @dp.callback_query_handler(text="g_dawamliligi")
    async def grafik_d(callback: CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("""
        <b>🎨 Grafik Dizayn</b>

        📅 Kurs dawamliligi: <b>4 ay</b>  
        📆 Haptede: <b>3 kun</b>  
        ⏰ Sabaq waqti: <b>17:00 – 19:00</b>  
        📖 <b>1-ay</b> — Design tiykarlari  
        🖌 Color, typography  
        📖 <b>2-ay</b> — Photoshop  
        📖 <b>3-ay</b> — Figma UI/UX  
        📖 <b>4-ay</b> — Portfolio project  
        🌟 Freelance is baslaw imkaniyati!
        """,reply_markup=back_grafik)

    @dp.callback_query_handler(text="d_dawamliligi")
    async def data_d(callback: CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("""
        <b>📊 Data Science</b>

        📅 Kurs dawamliligi: <b>7 ay</b>  
        📆 Haptede: <b>3 kun</b>  
        ⏰ Sabaq waqti: <b>19:00 – 21:00</b>  

        📖 <b>1-ay</b> — Python tiykarlari  
        🐍 Syntax, function, OOP  

        📖 <b>2-ay</b> — Matematika ham statistika  
        📈 Itimalliq, regressiya, analiz tiykarlari  

        📖 <b>3-ay</b> — Data analiz  
        📊 Pandas, NumPy, Matplotlib  

        📖 <b>4-5-ay</b> — Machine Learning  
        🤖 Scikit-learn, model quriw  

        📖 <b>6-7-ay</b> — Real joybar  
        🔬 Dataset menen toliq ameliy is  
        📁 Portfolio ushin project  

        🔥 Kurs aqirinda <b>Junior Data Analyst / ML Junior</b> darajasine shigiw imkaniyati!
        """,reply_markup=back_data)

    @dp.callback_query_handler(text="python_back")
    async def python_back_handler(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text(
            "<b>🐍 Python Backend</b>\n\nKerekli bolimdi saylan:",
            reply_markup=python_kurs,
        )
    @dp.callback_query_handler(text="frontend_back")
    async def frontend_back_handler(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text(
            "<b>💻 Frontend</b>\n\nKerekli bolimdi saylan:",
            reply_markup=frontend_kurs
        )
    @dp.callback_query_handler(text="grafik_back")
    async def grafik_back_handler(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text(
            "<b>🎨 Grafik dizayn</b>\n\nKerekli bolimdi saylan:",
            reply_markup=grafik_kurs
        )
    @dp.callback_query_handler(text="data_back")
    async def data_back_handler(callback: CallbackQuery):
        await callback.answer()
        await callback.message.edit_text(
            "<b>📊Data science</b>\n\nKerekli bolimdi saylan:",
            reply_markup=science_kurs,
        )

    @dp.callback_query_handler(text="p_bahasi")
    async def python_bahasi(callback: CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("""
            <b>💰 Python Backend kurs bahasi</b>

            📅 Toliq kurs bahasi: <b>3 800 000 sum</b>  
            
            💳 Bolip tolew imkaniyati:
            — Ayina: <b>650 000 sum</b>
            
            🎁 Aksiya:
            Birinshi 10 dana oqiwshiga <b>10% shegirme</b>
            
            📚 Baha ishine kiredi:
            ✅ Python ham Django / FastAPI
            ✅ Real backend joybarlar
            ✅ Database menen islew
            ✅ Mentor qadagalawi
            ✅ Sertifikat
            ✅ Jumisqa kiriwde jardem
            
            🚀 Junior Backend Developer darejesine shigin!""",reply_markup=back_python)
    @dp.callback_query_handler(text="f_bahasi")
    async def frontend_bahasi(callback: CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("""
        <b>💰 Frontend Development kurs bahasi</b>

        📅 Toliq kurs bahasi: <b>3 000 000 sum</b>  
        
        💳 Bolip tolew imkaniyati:
        — Ayina: <b>600 000 sum</b>
        
        🎁 Aksiya:
        Birinshi 10 dana oqiwshiga <b>10% shegirme</b>
        
        📚 Baha ishine kiredi:
        ✅ HTML, CSS, JavaScript
        ✅ React.js
        ✅ Responsive Web Design
        ✅ Real web joybarlar
        ✅ Portfolio tayarlaw
        ✅ Sertifikat
        
        🚀 Junior Frontend Developer bo‘ling!""",reply_markup=back_frontend)
    @dp.callback_query_handler(text="g_bahasi")
    async def grafik_bahasi(callback: CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("""
        <b>💰 Grafik Dizayn kurs bahasi</b>
        
        📅 Toliq kurs bahasi: <b>2 800 000 sum</b>  
        
        💳 Bolip tolew imkaniyati:
        — Ayina: <b>550 000 sum</b>
        
        🎁 Aksiya:
        Birinshi 10 dana oqiwshiga <b>10% shegirme</b>
        
        📚 Baha ishine kiredi:
        ✅ Photoshop ham Figma
        ✅ Logo ham branding
        ✅ Social media design
        ✅ Portfolio tayarlaw
        ✅ Freelancer jonelis
        
        🚀 Professional dizayner sipatinda start berin!""",reply_markup=back_grafik)

    @dp.callback_query_handler(text="d_bahasi")
    async def data_bahasi(callback: CallbackQuery):
        await callback.message.delete()
        await callback.message.answer("""
        <b>💰 Data Science kurs bahasi</b>

        📅 Toliq kurs bahasi: <b>4 200 000 sum</b>  
        
        💳 Bolip tolew imkaniyati:
        — Ayina: <b>750 000 sum</b>
        
        🎁 Aksiya:
        Birinshi 10 dana oqiwshiga <b>10% shegirme</b>
        
        📚 Baha ishine kiredi:
        ✅ Python Data Analysis
        ✅ Pandas, NumPy, Matplotlib
        ✅ Machine Learning tiykarlari
        ✅ Real dataset menen islew
        ✅ Portfolio project
        ✅ Sertifikat
        
        🚀 Junior Data Analyst / ML qaniygesi darejesine shigin!""",reply_markup=back_data)

    @dp.callback_query_handler(text="onlayn_kurs")
    async def onlain(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("""
            Siz kompyuterdi tusinbiysizba onda sizge kompyuter sawatqanligi kursimizdi usinamiz
            Siz IT tarawina ele qadem qoymadiniz, ham qaysi jonelisi tanlawdi bilmey atirsizba\n
            onda sizge IT foundation kursimizdi usinamiz""", reply_markup=onlayn_kurs)

    @dp.callback_query_handler(text="kompyuter")
    async def onlain_kom(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("""
            ✓ Kompyuter sawatxanlıǵı kursı;

        Eger siz kompyuterdi jetik úyreniwdi qáleseńiz, bul kurs áyne siz ushın!

        📌 Kurs dawamında siz tómendegilerdi úyrenesiz:

        ✅ Kompyuter tiykarı
        ✅ Windows sisteması menen islew
        ✅ Ord programmasında hújjetler tayarlaw
        ✅ Excel programmasında keste hám esap-kitaplar
        ✅ Internet hám brauzerler menen islew
        ✅ Fayllardı basqarıw
        ✅ Elektron pochta islew

        ✅ Kurs baslawshılar ushın arnalǵan. Aldın ala hesh qanday bilim talap etilmeydi.

        ➤ Kursti tamamlaģannan soń siz kompyuterden isenimli paydalanıw kónlikpesine iye bolasız!""",
                                        reply_markup=kompyuter_kurs)

    @dp.callback_query_handler(text="foundation")
    async def onlain_kom(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("""
        ️ IT Foundation kursı

        IT tarawına kiriwdi rejelestirip atırsız ba? Onda bul kurs siz ushın ideal baslanıw noqatı!
        
        📌 Kurs dawamında siz tómendegilerdi úyrenesiz:
        
        ✓ IT tiykarları hám zamanagóy texnologiyalar túsinigi;
        ➤ Kompyuter arxitekturası hám dástúriy támiynat.
        ✓ Fayl sisteması hám operacion sistema menen islew;
        ✓ Internet texnologiyaları tiykarları;
        ➤ Programmalastırıwģa kiriw (algoritm túsinikleri).
        ️ IT tarawında qollanılatuǵın tiykarǵı qurallar
        
        ✅ Kurs baslawshılar ushın sáykes keledi. Hesh qanday aldınǵı tájiriybe talap etilmeydi.
        
        🔥 Kursti tamamlaǵannan soń siz IT dúnyasına bekkem tiykar qoyǵan bolasız!""",reply_markup=foundation_kurs)

    @dp.callback_query_handler(text="komp_demo")
    async def onlain_kom5(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("KOmpyuter sawatqanligi kursi boyinsha\n"
                                  "demo sabaqlardi koriwiniz mumkin",reply_markup=komp_demo)

    @dp.message_handler(text="1-sabaq")
    async def demo_kom1(message: types.Message):
        await message.answer_video(video="BAACAgIAAxkBAAIE82mmzPjyUBeKElqhqBrQixsVY-wkAAKvUAAC8MqpS1yO1XLiU8eAOgQ",
                                   caption="Bul 1inshi demo sabaq")

    @dp.message_handler(text="4-sabaq")
    async def demo_kom4(message: types.Message):
        await message.answer_video(video="BAACAgIAAxkBAAIE8WmmzPFObeovkZja_GlCLb2jtaEiAAK6UAAC8MqpS2Py5CnmVVndOgQ",
                                   caption="Bul 4inshi demo sabaq")

    @dp.message_handler(text="12-sabaq")
    async def demo_kom12(message: types.Message):
        await message.answer_video(video="BAACAgIAAxkBAAIE72mmzOqcqRp2hdRfAkZyhg8gLplSAAKzVwACdIhQSbrv6xqQ1eAIOgQ",
                                   caption="Bul 12inshi demo sabaq")
    @dp.message_handler(text="Kompyuter kursqa qaytiw")
    async def komp_course_back(message:types.Message):
        await message.answer("Kompyuter sawatqanligi kursi",reply_markup=kompyuter_kurs)

    @dp.message_handler(text="Foundation kursqa qaytiw")
    async def komp_course_back(message: types.Message):
        await message.answer("IT Foundation kursi", reply_markup=foundation_kurs)

    @dp.callback_query_handler(text="foun_demo")
    async def onlain_kom5(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("IT foundation kursi boyinsha\n"
                                  "demo sabaqlardi koriwiniz mumkin", reply_markup=foun_demo)

    @dp.message_handler(text="1-demo sabaq")
    async def demo_kom1(message: types.Message):
        await message.answer_video(video="BAACAgIAAxkBAAIE6mmmy5lRtXKZ8eSyvMP-BhfcKdIcAALJnAACL-8wSZAEIsQ2PzGbOgQ",
                                            caption="Bul 1inshi demo sabaq")
    @dp.message_handler(text="2-demo sabaq")
    async def demo_kom1(message: types.Message):
        await message.answer_video(video="BAACAgIAAxkBAAIE5WmmyzT1LjgP2sRBtwhW0dOm_uQnAALVnAACL-8wSfIHrFnJkW6lOgQ",
                                   caption="Bul 2inshi demo sabaq")
    @dp.message_handler(text="3-demo sabaq")
    async def demo_kom1(message: types.Message):
        await message.answer_video(video="BAACAgIAAxkBAAIE7WmmzNiM0c4a1miOxRnXQHwHO-CBAALCnAACL-8wSd3lxB9xQIJgOgQ",
                                   caption="Bul 2inshi demo sabaq")
    @dp.callback_query_handler(text="komp_back")
    async def komp_back(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("""
                Siz kompyuterdi tusinbiysizba onda sizge kompyuter sawatqanligi kursimizdi usinamiz
                Siz IT tarawina ele qadem qoymadiniz, ham qaysi jonelisi tanlawdi bilmey atirsizba\n
                onda sizge IT foundation kursimizdi usinamiz""", reply_markup=onlayn_kurs)
    @dp.callback_query_handler(text="foun_back")
    async def foun_back(call: CallbackQuery):
        await call.message.delete()
        await call.message.answer("""
                Siz kompyuterdi tusinbiysizba onda sizge kompyuter sawatqanligi kursimizdi usinamiz
                Siz IT tarawina ele qadem qoymadiniz, ham qaysi jonelisi tanlawdi bilmey atirsizba\n
                onda sizge IT foundation kursimizdi usinamiz""", reply_markup=onlayn_kurs)

    @dp.callback_query_handler(text="komp_aliw")
    async def pay_kompyuter(callback: CallbackQuery):
        await bot.send_invoice(
            chat_id=callback.from_user.id,
            title="Kompyuter sawatxanlıǵı kursı",
            description="Kursqa jaziliw ushin to'lewdi amelge asirin'.",
            provider_token=CLICK_TOKEN,
            currency="UZS",
            prices=[LabeledPrice(label="Kompyuter kursi", amount=15000000)],  # 150 000 so'm
            payload="payload_komp",
            start_parameter="komp-course"
        )
        await callback.answer()

    @dp.callback_query_handler(text="foun_aliw")
    async def pay_foundation(callback: CallbackQuery):
        await bot.send_invoice(
            chat_id=callback.from_user.id,
            title="IT Foundation kursı",
            description="IT Foundation kursi ushin to'lew.",
            provider_token=CLICK_TOKEN,
            currency="UZS",
            prices=[LabeledPrice(label="Foundation kursi", amount=20000000)],  # 200 000 so'm
            payload="payload_foun",
            start_parameter="foun-course"
        )
        await callback.answer()

    @dp.pre_checkout_query_handler(lambda query: True)
    async def process_pre_checkout(pre_checkout_query: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

    @dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
    async def successful_payment(message: Message):
        payment = message.successful_payment

        kurs_nomi = "Kurs"
        if payment.invoice_payload == "payload_komp":
            kurs_nomi = "Kompyuter sawatxanlıǵı"
        elif payment.invoice_payload == "payload_foun":
            kurs_nomi = "IT Foundation"

        await message.answer(
            f"✅ To'lew tabisli amelge asirildi!\n\n"
            f"Siz '{kurs_nomi}' kursina jazildiniz.\n",
            reply_markup=onlayn_sabaq

        )














