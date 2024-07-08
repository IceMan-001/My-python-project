from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)

# кнопки для простой клавиатуры
kb = [
    [
        KeyboardButton(text="Погода"),
        KeyboardButton(text="Курс валют"),
        KeyboardButton(text="Вакансии")
    ]
]

# простая клавиатура
keyboard = ReplyKeyboardMarkup(
    keyboard=kb,
    resize_keyboard=True,  # масштабирование кнопок
    input_field_placeholder="Нажмите кнопку"
)


# Инлайн-клавиатура
def get_keyboard_inline():
    buttons = [
        [
            InlineKeyboardButton(text="Погода", callback_data="weather"),
            InlineKeyboardButton(text="Курс валют", callback_data="course"),
            InlineKeyboardButton(text="Вакансии", callback_data="vacancies"),
        ]
    ]
    inline_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return inline_keyboard


