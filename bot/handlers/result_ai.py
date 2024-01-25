from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram.filters import Command, StateFilter
from bot.services.services import analyses
from bot.states.result_state import ResultState
from bot.lexicon.en import LEXICON_EN, BUTTON
from bot.keyboard.keyboard_utils import create_result_step
from aiogram.fsm.state import default_state

result_router = Router()


@result_router.message(Command('result'), StateFilter(default_state))
@result_router.message(Command('result'), ~StateFilter(default_state))
@result_router.callback_query(F.data.in_(BUTTON['IMPORTANT'].keys()), ResultState.result)
async def process_final_result(callback: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    result = analyses(states.get('client_id'))
    if result:
        await state.update_data(result=result)
        await state.update_data(current_page=0)
        await state.update_data(res_len=len(result))
        text = '\n'.join((str(result[0][0]), str(result[0][1])))
        try:
            await callback.message.answer(text=LEXICON_EN['result'] + '\n' + text,
                                          reply_markup=create_result_step())
        except:
            await callback.answer(text=LEXICON_EN['result'] + '\n' + text,
                                          reply_markup=create_result_step())
    else:
        try:
            await callback.message.answer(text='Currently you don`t have result. Try /run_quiz')
        except:
            await callback.answer(text='Currently you don`t have result. Try /run_quiz')


@result_router.callback_query(F.data == 'prev')
async def prev_result(callback: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    values = ResultState.get_state_values(states)
    result, current_page = values.get('result'), values['current_page']
    if current_page > 0:
        current_page -= 1
        text = '\n'.join((str(result[current_page][0]), str(result[current_page][1])))
        await state.update_data(current_page=current_page)
        await callback.message.edit_text(text=text,
                                         reply_markup=create_result_step())


@result_router.callback_query(F.data == 'next')
async def next_result(callback: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    values = ResultState.get_state_values(states)
    result, current_page, res_len = values.get('result'), values['current_page'], values.get('res_len')
    if current_page < res_len - 1:
        current_page += 1
        text = '\n'.join((str(result[current_page][0]), str(result[current_page][1])))
        await state.update_data(current_page=current_page)
        await callback.message.edit_text(text=text,
                                         reply_markup=create_result_step())


@result_router.callback_query(F.data == 'reason')
async def reason_desc(callback: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    values = ResultState.get_state_values(states)
    await callback.message.edit_text(
        text=values.get('result')[values.get('current_page')][7],
        reply_markup=create_result_step()
    )


@result_router.callback_query(F.data == 'srl')
async def salary_latvia_desc(callback: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    values = ResultState.get_state_values(states)
    result, current_page = values.get('result'), values['current_page']
    salary_range = '\tSalary in Latvia:\n' + ' - '.join((str(result[current_page][5]), str(result[current_page][6])))
    await callback.message.edit_text(
        text=salary_range,
        reply_markup=create_result_step()
    )


@result_router.callback_query(F.data == 'srg')
async def salary_germany_desc(callback: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    values = ResultState.get_state_values(states)
    result, current_page = values.get('result'), values['current_page']
    salary_range = '\tSalary in Germany:\n' + ' - '.join((str(result[current_page][3]), str(result[current_page][4])))
    await callback.message.edit_text(
        text=salary_range,
        reply_markup=create_result_step()
    )


@result_router.callback_query(F.data == 'full_desc')
async def full_desc(callback: CallbackQuery, state: FSMContext):
    states = await state.get_data()
    values = ResultState.get_state_values(states)
    result, current_page = values.get('result'), values['current_page']
    await callback.message.edit_text(
        text='\tFull description:\n' + result[current_page][2],
        reply_markup=create_result_step()
    )
