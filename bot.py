import telebot
import config
from schedule_logic import ScheduleLogic

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, config.HELLO_TEXT_LABEL)
    bot.send_message(message.chat.id, config.INPUT_TEXT_LABEL)


@bot.message_handler(content_types=['text'])
def get_schedule(message):
    if message.chat.type != 'private':
        return

    date = ScheduleLogic.read_date(message.text)

    if not ScheduleLogic.is_date_parsed(date):
        bot.send_message(message.chat.id, config.WRONG_DATE_LABEL)
        bot.send_message(message.chat.id, config.INPUT_TEXT_LABEL)
        return

    if ScheduleLogic.is_date_before_works_founded(date):
        bot.send_message(message.chat.id, config.TOO_OLD_DATE_REPLY_LABEL.format(date.strftime('%d.%m.%Y')),
                         parse_mode='Markdown')
    else:
        shifts_scheme = ScheduleLogic.get_shifts_scheme(date)
        reply = ScheduleLogic.get_reply(date, shifts_scheme)
        bot.send_message(message.chat.id, reply, parse_mode='Markdown')

    menu = telebot.types.InlineKeyboardMarkup()
    menu.add(telebot.types.InlineKeyboardButton(config.YES_NO_ANSWERS_LABELS[0], callback_data='yes'))
    bot.send_message(message.chat.id, config.DO_AGAIN_LABEL, reply_markup=menu)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == 'yes':
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=config.DO_AGAIN_LABEL, reply_markup=None)
            bot.send_message(call.message.chat.id, config.INPUT_TEXT_LABEL)


bot.polling(none_stop=True)



