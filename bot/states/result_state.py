from aiogram.fsm.state import State, StatesGroup
from typing import Union


class ResultState(StatesGroup):
    result = State()
    current_page = State()
    res_len = State()

    @classmethod
    def get_state_values(cls, state: dict) -> Union[bool, dict]:
        """Get self values from fsm
        :param state: dict - Dict generate from fsm with function .get_data()
        """
        __fields = (field.split(':')[1] for field in cls.__state_names__)
        __values = {key: state.get(key) for key in __fields}
        if len(__values):
            return __values
