from aiogram.fsm.state import State, StatesGroup

class RegisterStates(StatesGroup):
    ism=State()
    familiya=State()
    otasining_ismi=State()
    jinsi=State()
    guruh=State()
    kurs=State()
    tel=State()
    confirm=State()