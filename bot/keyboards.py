from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton




info_buttons=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ma'lumotlarni ko'rish",callback_data="user_info")]
    ]
)

tel_button=ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Telefon raqamni yuborish",request_contact=True)]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

confirm_button=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Saqlansin",callback_data="yes")],
        [InlineKeyboardButton(text="Bekor qilinsin",callback_data="no")]
    ]
)

jins_button=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Erkak",callback_data="erkak")],
        [InlineKeyboardButton(text="Ayol", callback_data="ayol")]
    ]
)