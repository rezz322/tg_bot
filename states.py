from aiogram.fsm.state import State, StatesGroup

class AdminStates(StatesGroup):
    waiting_for_user_id = State()
    waiting_for_account_number = State()
    waiting_for_give_key_user = State()
    waiting_for_give_key_number = State()
