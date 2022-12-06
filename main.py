import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram.ext import Updater, CommandHandler, CallbackContext, Filters, MessageHandler, CallbackQueryHandler
from my_token import my_token
from logger import log


def help_command(update: Update, context: CallbackContext):
    log(update)
    update.message.reply_text(f'{update.effective_user.first_name}! Я умею:\n'
                                    f'1. Считать целые числа. Введите: /1 2 + 2 \n'
                                    f'2. Считать рациональные числа. Введите: /2 1.2 - 2.2 \n'
                                    f'3. Считать комлексные числа. Введите: /3 (1+2j) / (1+2j) \n'
                                    f'Не забудьте между цифрами указать нужную операцию через пробел +,-,/,*')

def int_command(update: Update, context: CallbackContext):
    log(update)
    msg = update.message.text
    print(msg)

    a = int(context.args[0])
    operator = context.args[1]
    b = int(context.args[2])

    if operator == "+":
        update.message.reply_text(f'{a} {operator} {b} = {a + b}')
    elif operator == "-":
        update.message.reply_text(f'{a} {operator} {b} = {a - b}')
    elif operator == "*":
        update.message.reply_text(f'{a} {operator} {b} = {a * b}')
    elif operator == "/":
        update.message.reply_text(f'{a} {operator} {b} = {a / b}')

def float_command(update: Update, context: CallbackContext):
    log(update)
    msg = update.message.text
    print(msg)

    a = float(context.args[0])
    operator = context.args[1]
    b = float(context.args[2])

    if operator == "+":
        update.message.reply_text(f'{a} {operator} {b} = {round(a + b, 4)}')
    elif operator == "-":
        update.message.reply_text(f'{a} {operator} {b} = {round(a - b, 4)}')
    elif operator == "*":
        update.message.reply_text(f'{a} {operator} {b} = {round(a * b, 4)}')
    elif operator == "/":
        update.message.reply_text(f'{a} {operator} {b} = {round(a / b, 4)}')

def complex_command(update: Update, context: CallbackContext):
    log(update)
    msg = update.message.text
    print(msg)

    a = complex(context.args[0])
    operator = context.args[1]
    b = complex(context.args[2])

    if operator == "+":
        update.message.reply_text(f'{a} {operator} {b} = {a + b}')
    elif operator == "-":
        update.message.reply_text(f'{a} {operator} {b} = {a - b}')
    elif operator == "*":
        update.message.reply_text(f'{a} {operator} {b} = {a * b}')
    elif operator == "/":
        update.message.reply_text(f'{a} {operator} {b} = {a / b}')

updater = Updater(my_token())

def start_command(update: Update, context: CallbackContext):
    buttonA = telegram.InlineKeyboardButton('Помощь', callback_data='buttonA')
    buttonB = telegram.InlineKeyboardButton('Калькулятор целых чисел', callback_data='buttonB')
    buttonC = telegram.InlineKeyboardButton('Калькулятор рациональных чисел', callback_data='buttonC')
    buttonD = telegram.InlineKeyboardButton('Калькулятор комплексных чисел', callback_data='buttonD')
    markup = telegram.InlineKeyboardMarkup(inline_keyboard=[[buttonA], [buttonB], [buttonC], [buttonD]])

    update.message.reply_text(f'Привет, {update.effective_user.first_name}. Нажми нужную тебе кнопку ниже',
                              reply_markup=markup)
    return callback

def callback(update: Update, context: CallbackContext):
    query = update.callback_query
    variant = query.data
    if variant == 'buttonA':
        query.answer()
        query.edit_message_text(text='Если вам нужна помощь в командах. Нажмите /help')

    if variant == 'buttonB':
        query.answer()
        query.edit_message_text(text='Чтобы произвести расчет с целыми числами введите: /1 2 + 2'\
            '\nНе забудьте между цифрами указать нужную операцию через пробел +,-,/,*')
    
    if variant == 'buttonC':
        query.answer()
        query.edit_message_text(text='Чтобы произвести расчет с раиональными числами введите: /2 1.2 * 2.2'\
            '\nНе забудьте между цифрами указать нужную операцию через пробел +,-,/,*')

    if variant == 'buttonD':
        query.answer()
        query.edit_message_text(text='Чтобы произвести расчет с целыми числами введите: /3 (1+2j) / (1+2j)'\
            '\nНе забудьте между цифрами указать нужную операцию через пробел +,-,/,*')

updater.dispatcher.add_handler(CommandHandler('start', start_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('1', int_command))
updater.dispatcher.add_handler(CommandHandler('2', float_command))
updater.dispatcher.add_handler(CommandHandler('3', complex_command))
updater.dispatcher.add_handler(CallbackQueryHandler(callback=callback, pattern=None, run_async=False)
)

print('работает')
updater.start_polling()
updater.idle()