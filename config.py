from datetime import datetime

TOKEN = ""

# constants

SCHEDULE_SCHEME = [2, 4, 1, 2, 3, 1, 2, 3, 4, 2, 3, 4, 1, 3, 4, 1]
FOUNDING_DATE = datetime(1984, 10, 15)

# text labels

HELLO_TEXT_LABEL = "Добро пожаловать! Я — бот, и я могу подсказать вам, как будут работать бригады по графику №3."
INPUT_TEXT_LABEL = "Какая дата вас интересует?"
TOO_OLD_DATE_REPLY_LABEL = "*{}* никто не работал. Завод еще не построили 😆"
WRONG_DATE_LABEL = "Когда, когда? Я не понимаю. Давайте попробуем еще раз. Введите дату в формате ДД.ММ.ГГГГ."
SCHEDULE_OUTPUT_LABEL = "*{}* бригады {} так:\n-----------------------------\n1️⃣ Бригада - {}\n2️⃣ Бригада - {}\n" \
                        "3️⃣ Бригада - {}\n4️⃣ Бригада - {}\n-----------------------------"
DO_AGAIN_LABEL = "Хотите проверить еще дату?"
YES_NO_ANSWERS_LABELS = ["Да", "Нет"]
PAST_PRESENT_VERBS = ["работали", "работают"]
SHIFTS_LABELS = {
    1: "🌞 День️",
    2: "🌜 Ночь",
    3: "😴 Отсыпной",
    4: "⛱ Выходной"
}
