from aiogram.types import (Message, CallbackQuery)
from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram import Router, F

from bot.config.config import db_config
from bot.models.methods import DatabaseCursor
from bot.states.quiz_state import QuizState
from bot.states.result_state import ResultState
from bot.states.user_state import UserState

from bot.lexicon.en import LEXICON_EN, BUTTON
from bot.keyboard.keyboard_utils import create_inline_kb, create_bool_kb, create_quiz_kb

router = Router()
database:  DatabaseCursor = DatabaseCursor(db_config())


@router.message(CommandStart(), StateFilter(default_state))
@router.message(CommandStart(), ~StateFilter(default_state))
async def process_start_command(message: Message, state: FSMContext):
    """
        Handler for cmd /start. Checking for client presence in DB, if client exist start quiz
        else start user config questions like name, language
    """
    await state.clear()
    await state.update_data(client_id=message.from_user.id)
    client_config = database.get_user_config(message.from_user.id)
    prof_count = database.get_profession_count()
    await state.update_data(job_count=prof_count)
    if not client_config:
        await message.answer(text=LEXICON_EN['language'], reply_markup=create_inline_kb(4, **BUTTON['LANGUAGE']))
        await state.set_state(UserState.language)
    else:
        await state.update_data(name=client_config[1], language=client_config[0])
        await message.answer(text=LEXICON_EN['conest_save'].format(name=client_config[1],
                                                                   count=prof_count),
                             reply_markup=create_bool_kb())
        await state.set_state(UserState.consest)


@router.message(Command('language'), StateFilter(default_state))
@router.message(Command('language'), ~StateFilter(default_state))
async def process_language_command_message(message: Message, state: FSMContext):
    """Cmd for create state to setting language"""
    await message.answer(text=LEXICON_EN['language'], reply_markup=create_inline_kb(4, **BUTTON['LANGUAGE']))
    await state.set_state(UserState.language)


@router.callback_query(F.data.in_(BUTTON['LANGUAGE'].keys()), UserState.language)
async def process_language_command(callback: CallbackQuery, state: FSMContext):
    """Handler for state language and move to state name"""
    await state.update_data(language=callback.data)
    await callback.message.answer(text=LEXICON_EN['welcome'])
    await state.set_state(UserState.name)


@router.message(F.text, UserState.name)
async def process_name_command(message: Message, state: FSMContext):
    """Handler for state name and move to state consest. Also create new row in DB table client"""
    await state.update_data(name=message.text)
    data = await state.get_data()
    if not message.text.startswith('/'):
        database.create_client(client_id=data.get('client_id'), name=data.get('name'),
                               language=data.get('language'))
    await message.answer(text=LEXICON_EN['conest_save'].format(name=data.get('name'),
                                                               count=data.get('job_count')),
                         reply_markup=create_bool_kb())
    await state.set_state(UserState.consest)


@router.callback_query(F.data.in_(BUTTON['IMPORTANT'].keys()), UserState.consest)
async def process_consest_command(callback: CallbackQuery, state: FSMContext):
    """Handler for state consest if answer yes and move to state age else end quit from quiz"""
    if callback.data == '1':
        await callback.message.answer(text=LEXICON_EN['social'], reply_markup=create_quiz_kb(
            'social'))
        await state.set_state(QuizState.social)
    else:
        await state.clear()
        await callback.message.answer(text=LEXICON_EN['no_consest'])


@router.message(Command('run_quiz'), StateFilter(default_state))
@router.message(Command('run_quiz'), ~StateFilter(default_state))
async def process_quiz_command(message: Message, state: FSMContext):
    """Cmd for start quiz"""
    client_config = database.get_user_config(message.from_user.id)
    if client_config:
        await message.answer(text=LEXICON_EN['social'], reply_markup=create_quiz_kb(
            'social'))
        await state.set_state(QuizState.social)
    else:
        await message.answer('Sorry, but first answer a few simple questions <a>/start</a>')
