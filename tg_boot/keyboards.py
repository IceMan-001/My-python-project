from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardButton

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


menu_items = ['Погода', 'Курс', 'Вакансии', ]


# Keyboard Builder
async def menu_items_builder():
    keyboard_builder = ReplyKeyboardBuilder()
    for menu_item in menu_items:
        keyboard_builder.add(KeyboardButton(text=menu_item, resize_keyboard=True))
    return keyboard_builder.adjust(3).as_markup()
