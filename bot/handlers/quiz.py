from aiogram.types import (CallbackQuery)
from aiogram.fsm.context import FSMContext
from aiogram import Router, F
from bot.states.quiz_state import QuizState
from bot.handlers.user_handler import database
from bot.lexicon.en import LEXICON_EN
from bot.keyboard.keyboard_utils import create_quiz_kb, create_inline_kb, create_bool_kb
from bot.services.services import step_result
from bot.states.result_state import ResultState

router_quiz = Router()


async def simple_handler(callback: CallbackQuery,
                         state: FSMContext,
                         current_state: str,
                         next_state: str,
                         count_state: str):
    await state.update_data(**{current_state: callback.data})
    data = await state.get_data()
    await state.update_data(**{count_state: int((data.get(count_state, 0)) + int(callback.data))})
    await callback.message.answer(text=LEXICON_EN[next_state], reply_markup=create_quiz_kb(next_state))
    await state.set_state(getattr(QuizState, next_state))


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.social)
async def process_social_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'social', 'group_size', 'client_type')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.group_size)
async def process_group_size_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'group_size', 'relax_time', 'client_type')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.relax_time)
async def process_relax_time_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'relax_time', 'meeting', 'client_type')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.meeting)
async def process_meeting_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'meeting', 'share', 'client_type')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.share)
async def process_share_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'share', 'focus', 'client_type')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.focus)
async def process_focus_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'focus', 'plan', 'client_choise')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.plan)
async def process_plan_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'plan', 'discussion', 'client_choise')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.discussion)
async def process_discussion_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'discussion', 'enjoyment', 'client_choise')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.enjoyment)
async def process_enjoyment_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'enjoyment', 'learning', 'client_choise')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.learning)
async def process_learning_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'learning', 'decision', 'client_choise')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.decision)
async def process_decision_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'decision', 'disagreement', 'client_decision')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.disagreement)
async def process_disagreement_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'disagreement', 'assess_performance', 'client_decision')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.assess_performance)
async def process_assess_perfom_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'assess_performance', 'leadership', 'client_decision')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.leadership)
async def process_leadership_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'leadership', 'feedback', 'client_decision')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.feedback)
async def process_feedback_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'feedback', 'work_time', 'client_decision')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.work_time)
async def process_work_time_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'work_time', 'deadline', 'client_perceiving')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.deadline)
async def process_deadline_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'deadline', 'rules', 'client_perceiving')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.rules)
async def process_rooles_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'rules', 'vacation', 'client_perceiving')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.vacation)
async def process_vacation_question(callback: CallbackQuery, state: FSMContext):
    await simple_handler(callback, state, 'vacation', 'satisfaction', 'client_perceiving')


@router_quiz.callback_query(F.data.in_(('1', '-1')), QuizState.satisfaction)
async def process_satisfaction_question(callback: CallbackQuery, state: FSMContext):
    await state.update_data(satisfaction=callback.data)
    data = await state.get_data()
    client_perceiving = int(data.get('client_perceiving', 0)) + int(callback.data)
    await state.update_data(client_perceiving=client_perceiving)
    result_out = ''
    options = {
        'client_type': ('I', 'E'),
        'client_choise': ('S', 'N'),
        'client_decision': ('T', 'F'),
        'client_perceiving': ('J', 'P')
    }
    data = await state.get_data()
    for key, value in options.items():
        result = step_result(data.get(key), value)
        result_out += result
    database.quiz_field_up(database.get_client_id(data.get('client_id')), result_out)
    await callback.message.answer(text=LEXICON_EN['client_perceiving'] + result_out +
                                  '\nDo you want to see the best job offers?',
                                  reply_markup=create_bool_kb())
    await state.set_state(ResultState.result)
