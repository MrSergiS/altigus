from aiogram.fsm.state import State, StatesGroup


class UserState(StatesGroup):
    client_id = State()
    language = State()
    name = State()
    consest = State()
    final = State()
    recommend = State()
    job_count = State()
    best_job = State()
