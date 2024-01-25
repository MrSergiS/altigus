from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.lexicon.en import BUTTON


def create_inline_kb(width: int, *args: str, **kwargs: str) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=BUTTON.get(button, button),
                callback_data=button
            ))

    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button
            ))

    kb_builder.row(*buttons, width=width)
    return kb_builder.as_markup()


def create_bool_kb():
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_yes = InlineKeyboardButton(
        text='👍Yes',
        callback_data='1'
    )

    button_no = InlineKeyboardButton(
        text='👎No',
        callback_data='0'
    )
    kb_builder.row(button_yes, button_no, width=2)
    return kb_builder.as_markup()


def create_quiz_kb(key: str):
    texts = BUTTON.get(key)
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    button_yes = InlineKeyboardButton(
        text=texts[0],
        callback_data='-1'
    )

    button_no = InlineKeyboardButton(
        text=texts[1],
        callback_data='1'
    )
    kb_builder.row(button_yes, button_no, width=2)
    return kb_builder.as_markup()


def create_result_step():
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    buttons = [
        InlineKeyboardButton(
            text='Full description',
            callback_data='full_desc'
        ),
        InlineKeyboardButton(
            text='Salary range Latvia',
            callback_data='srl'
        ),
        InlineKeyboardButton(
            text='Salary range Germany',
            callback_data='srg'
        ),
        InlineKeyboardButton(
            text='Why it`s your best reason',
            callback_data='reason'
        ),
        InlineKeyboardButton(
            text='<<',
            callback_data='prev'
        ),
        InlineKeyboardButton(
            text='>>',
            callback_data='next'
        ),
    ]
    kb_builder.row(*buttons[0:4], width=1)
    kb_builder.row(*buttons[4:6], width=2)
    return kb_builder.as_markup()


