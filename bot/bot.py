import asyncio
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from os import getenv
from dotenv import load_dotenv
from functions import *
from keyboards import *
from states import RegisterStates


load_dotenv()
bot=Bot(token=getenv("TOKEN"))
dp=Dispatcher()

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    result=await asyncio.to_thread(check_bot_user,message.from_user.id)
    if not result:
        await asyncio.to_thread(
            add_bot_user,
            message.from_user.id,
            message.from_user.username
            )
    await message.answer(
        "Assalomu alaykum.\n"
        "Bu bot orqali kutubxonamiz tizimdan ro'yhatdan o'tishingiz va kutubxonada mavjud kitoblar ro'yhatini ko'rishingiz mumkin.\n"
        "/start_registration - registratsiyadan o'tish\n"
        "/books - kutubxonadagi kitoblar ro'yhati"
    )

@dp.message(Command("books"))
async def books_handler(message: types.Message, state: FSMContext):
    await state.clear()
    kitoblar=get_kitoblar()
    if not kitoblar:
        await message.answer(
            "Kitoblar mavjud emas yoki kiritilmagan, yoki tizimda nosozlik mavjud.\n\n"
            "Iltimos adminga murojaat qiling: @shuhratrozimatov"
        )
        return
    await state.update_data(kitoblar=kitoblar)
    
    total_books = len(kitoblar)
    total_pages = (total_books + 4) // 5  

    builder = InlineKeyboardBuilder()

    for i in range(1, total_pages + 1):
        builder.button(
            text=str(i),
            callback_data=f"books_page:{i}"
        )

    builder.adjust(5)
    page_buttons=builder.as_markup()

    await state.update_data(page_buttons=page_buttons)

    text=(
        "Kutubxona tizimida mavjud kitoblar:\n"
        "--------------------------------------\n"
        )
    space="\u00A0"
    for kitob in kitoblar[:5]:
        text+=(
            f"{space*4}Nomi: <b>{kitob['nomi']}</b>\n"
            f"{space*4}Muallif: <b>{kitob['muallif']['ism']} {kitob['muallif']['familiya']}</b>\n"
            f"{space*4}Janr: <b>{kitob['janr']}</b>\n"
            f"{space*4}Sahifa: <b>{kitob['sahifa']}</b>\n"
            "--------------------------------------\n"
        )
    msg=await message.answer(
        text,
        reply_markup=page_buttons,
        parse_mode='HTML'
    )
    await state.update_data(last_msg_id=msg.message_id)

@dp.callback_query(F.data.startswith("books_page:"))
async def books_page_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    page=int(callback.data.split(":")[1])
    data=await state.get_data()
    kitoblar=data['kitoblar']
    last_msg_id=data['last_msg_id']
    page_buttons=data['page_buttons']
    space="\u00A0"
    start=5*(page-1)
    end=5*page
    text=(
        "Kutubxona tizimida mavjud kitoblar:\n"
        "--------------------------------------\n"
        )
    for kitob in kitoblar[start:end]:
        text+=(
            f"{space*4}Nomi: <b>{kitob['nomi']}</b>\n"
            f"{space*4}Muallif: <b>{kitob['muallif']['ism']} {kitob['muallif']['familiya']}</b>\n"
            f"{space*4}Janr: <b>{kitob['janr']}</b>\n"
            f"{space*4}Sahifa: <b>{kitob['sahifa']}</b>\n"
            "--------------------------------------\n"
        )
    await bot.edit_message_text(
        chat_id=callback.message.chat.id,
        message_id=last_msg_id,
        text=text,
        reply_markup=page_buttons,
        parse_mode='HTML'
    )

@dp.message(Command("start_registration"))
async def start_registration_handler(message: types.Message, state: FSMContext):
    await state.clear()
    result=check_registration(message.from_user.id)
    if result:
        await message.answer("Siz ro'yhatdan o'tgansiz!",reply_markup=info_buttons)
    else:
        await message.answer(
            "Ro'yhatdan o'tish boshlandi!\n\n"
            "- Ismingizni kiriting:"
            )
        
        await state.set_state(RegisterStates.ism)

@dp.message(RegisterStates.ism)
async def registration_ism_handler(message: types.Message, state: FSMContext):
    await state.update_data(ism=message.text)
    await message.answer("- Familiyangizni kiriting:")
    await state.set_state(RegisterStates.familiya)

@dp.message(RegisterStates.familiya)
async def registration_fam_handler(message: types.Message, state: FSMContext):
    await state.update_data(familiya=message.text)
    await message.answer("- Otangizni ismini kiriting (Ismdan keyin o'g'li yoki qizi deb qo'shing):")
    await state.set_state(RegisterStates.otasining_ismi)

@dp.message(RegisterStates.otasining_ismi)
async def registration_o_ism_handler(message: types.Message, state: FSMContext):
    await state.update_data(otasining_ismi=message.text)
    await message.answer("- Jinsingiz kiriting:",reply_markup=jins_button)
    await state.set_state(RegisterStates.jinsi)

@dp.message(RegisterStates.jinsi)
async def registration_jins_handler(message: types.Message, state: FSMContext):
    await message.answer("- Jinsingiz kiriting:",reply_markup=jins_button)

@dp.callback_query(RegisterStates.jinsi)
async def registration_jins1_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await state.update_data(jinsi=callback.data)
    await callback.message.answer("- Guruhingizni kiriting:")
    await state.set_state(RegisterStates.guruh)

@dp.message(RegisterStates.guruh)
async def registration_guruh_handler(message: types.Message, state: FSMContext):
    await state.update_data(guruh=message.text)
    await message.answer("- Kursingizni kiriting:")
    await state.set_state(RegisterStates.kurs)

@dp.message(RegisterStates.kurs)
async def registration_kurs_handler(message: types.Message, state: FSMContext):
    if message.text.isdigit():
        if 0<int(message.text)<8:
            await state.update_data(kurs=int(message.text))
            await message.answer("- Telefoningizni kiriting:",reply_markup=tel_button)
            await state.set_state(RegisterStates.tel)
            return
    
    await message.answer("Iltimos kurs qiymatiga butun va 0dan katta lekin 8dan kichik son kiriting.")

@dp.message(RegisterStates.tel)
async def registration_tel_handler(message: types.Message, state: FSMContext):
    if message.contact:
        tel=message.contact.phone_number
    else:
        tel=message.text
    await state.update_data(tel=tel)
    data=await state.get_data()
    space="\u00A0"
    await message.answer(
        "ℹ️ Kiritilgan ma'lumotlar:\n\n"
        f"{space*4}Ism: <b>{data['ism']}</b>\n"
        f"{space*4}Familiya: <b>{data['familiya']}</b>\n"
        f"{space*4}Otasining ismi: <b>{data['otasining_ismi']}</b>\n"
        f"{space*4}Jinsi: <b>{data['jinsi']}</b>\n"
        f"{space*4}Guruh: <b>{data['guruh']}</b>\n"
        f"{space*4}Kurs: <b>{data['kurs']}</b>\n"
        f"{space*4}Tel: <b>{data['tel']}</b>\n\n"
        "- Saqlansinmi?",
        reply_markup=confirm_button,
        parse_mode="HTML"
    )
    await state.set_state(RegisterStates.confirm)

@dp.callback_query(F.data.in_(["yes","no"]))
async def confirm_handler(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    if callback.data == "yes":
        data=await state.get_data()
        result=register(
            telegram_id=callback.from_user.id,
            ism=data['ism'],
            familiya=data['familiya'],
            otasining_ismi=data['otasining_ismi'],
            jinsi=data['jinsi'],
            guruh=data['guruh'],
            kurs=data['kurs'],
            tel=data['tel']
        )
        if result:
            await callback.message.answer("Ma'lumot saqlandi ✅")
        else:
            await callback.message.answer(
                "Qandaydir xatolik yuz berdi, iltimos adminga murojaat qiling.\n"
                "@shuhratrozimatov"
                )
    elif callback.data == "no":
        await callback.message.answer("Joriy ro'yhatdan o'tish bekor qilindi, qayta o'tish uchun ustiga bosing: /start_registration")
    
    await state.clear()

@dp.callback_query(F.data == "user_info")
async def user_info_handler(callback: types.CallbackQuery):
    await callback.answer()
    data = get_user_info(callback.from_user.id)
    space="\u00A0"
    await callback.message.answer(
        "ℹ️ Ma'lumotlaringiz:\n\n"
        f"{space*4}Ism: <b>{data['ism']}</b>\n"
        f"{space*4}Familiya: <b>{data['familiya']}</b>\n"
        f"{space*4}Otasining ismi: <b>{data['otasining_ismi']}</b>\n"
        f"{space*4}Jinsi: <b>{data['jinsi']}</b>\n"
        f"{space*4}Guruh: <b>{data['guruh']}</b>\n"
        f"{space*4}Kurs: <b>{data['kurs']}</b>\n"
        f"{space*4}Tel: <b>{data['tel']}</b>",
        parse_mode='HTMl'
    )



async def main():
    print("Bot ishga tushdi!")
    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())