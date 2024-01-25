from aiogram.fsm.state import State, StatesGroup
from typing import Union


class QuizState(StatesGroup):
    social = State()
    group_size = State()
    relax_time = State()
    meeting = State()
    share = State()
    client_type = State()
    focus = State()
    plan = State()
    discussion = State()
    enjoyment = State()
    learning = State()
    client_choise = State()
    decision = State()
    disagreement = State()
    assess_performance = State()
    leadership = State()
    feedback = State()
    client_decision = State()
    work_time = State()
    deadline = State()
    rules = State()
    vacation = State()
    satisfaction = State()
    client_perceiving = State()

    @classmethod
    def get_state_values(cls, state: dict) -> Union[bool, dict]:
        """Get self values from fsm
        :param state: dict - Dict generate from fsm with function .get_data()
        """
        __fields = (field.split(':')[1] for field in cls.__state_names__)
        __values = {key: state.get(key) for key in __fields}
        if len(__values):
            return __values
        return False
