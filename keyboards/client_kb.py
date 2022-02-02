from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/work_time')
b2 = KeyboardButton('/location')
b3 = KeyboardButton('/menu')
b4 = KeyboardButton('/loadData')
b5 = KeyboardButton('cancel')
# b4 = KeyboardButton('Поделится номером', request_contact=True)
# b5 = KeyboardButton('Send location', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.row(b1, b2, b3).row(b4, b5)

