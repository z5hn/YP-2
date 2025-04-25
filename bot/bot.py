import telebot

TOKEN = "7551128400:AAFwdQcOZs6zoAp0xBBCcL7Zbd2KejcLzM4"
bot = telebot.TeleBot(TOKEN)

user_data = {}

def create_keyboard():
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = telebot.types.KeyboardButton("/balance")
    button2 = telebot.types.KeyboardButton("/history")
    button3 = telebot.types.KeyboardButton("/total")
    button4 = telebot.types.KeyboardButton("/clear")
    button5 = telebot.types.KeyboardButton("Добавить операцию (сумма, описание)")  # Кнопка для /add

    markup.add(button1, button2, button3, button4, button5)
    return markup


# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = {
            "balance": 0,
            "history": []
        }

    gif_id = "https://99px.ru/sstorage/86/2020/02/11102201155383879.gif"
    bot.send_animation(message.chat.id, gif_id)

    markup = create_keyboard()
    bot.reply_to(message, "Привет! Я бот учёта бюджета 💰\n\n"
                          "Доступные команды:", reply_markup=markup)


# команда /add
@bot.message_handler(func=lambda message: message.text == "Добавить операцию (сумма, описание)")
def ask_for_add(message):
    bot.reply_to(message, "Введите сумму и описание операции, например: '+500 подработка', или '-200 кофе'.")




@bot.message_handler(func=lambda message: message.text.startswith(('+', '-')))
def add_transaction(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        user_data[user_id] = \
        {
            "balance": 0,
            "history": []
        }

    try:
        parts = message.text.split(maxsplit=1)
        if len(parts) < 2:
            raise ValueError("Неверный формат. Используй: сумма, описание")

        amount = float(parts[0])
        description = parts[1]

        user_data[user_id]["balance"] += amount
        (user_data[user_id]["history"].append
        ({
            "amount": amount,
            "description": description
        }))

        sign = "доход" if amount > 0 else "расход"
        bot.reply_to(message, f"✅ {sign} на {abs(amount)}₽ добавлен:  {description}")
    except Exception as e:
        bot.reply_to(message, f"⚠️ Ошибка: Неверный формат. Используй: сумма, описание")


    markup = create_keyboard()
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)


# Команда /balance
@bot.message_handler(commands=['balance'])
def show_balance(message):
    user_id = message.from_user.id
    if user_id not in user_data:
        bot.reply_to(message, "Нет данных. Добавь первую операцию командой /add.")
        return

    balance = user_data[user_id]["balance"]
    bot.reply_to(message, f"💰 Текущий баланс: {balance:.2f}₽")

    markup = create_keyboard()
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)


# Команда /history
@bot.message_handler(commands=['history'])
def show_history(message):
    user_id = message.from_user.id
    if user_id not in user_data or not user_data[user_id]["history"]:
        bot.reply_to(message, "🗑 История пуста.")
        return

    history_text = "🧾 История операций:\n"
    for entry in user_data[user_id]["history"][-5:]:
        amt = entry["amount"]
        desc = entry["description"]
        sign = "+" if amt > 0 else "-"
        history_text += f"{sign}{abs(amt)}₽ — {desc}\n"

    bot.reply_to(message, history_text)

    markup = create_keyboard()
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)


# Команда /clear
@bot.message_handler(commands=['clear'])
def clear_history(message):
    user_id = message.from_user.id
    if user_id in user_data:
        user_data[user_id]["balance"] = 0
        user_data[user_id]["history"] = []
        bot.reply_to(message, "🧹 История очищена. Баланс сброшен до 0.")
    else:
        bot.reply_to(message, "🧹 Нет данных для очистки.")

    markup = create_keyboard()
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)


# Команда /total
@bot.message_handler(commands=['total'])
def show_totals(message):
    user_id = message.from_user.id
    if user_id not in user_data or not user_data[user_id]["history"]:
        bot.reply_to(message, "🗑 Нет данных.")
        return

    income = sum(entry["amount"] for entry in user_data[user_id]["history"] if entry["amount"] >= 0)
    expense = sum(entry["amount"] for entry in user_data[user_id]["history"] if entry["amount"] < 0)

    bot.reply_to(message, f"📊 Всего доходов: +{income:.2f}₽\n"
                          f"💸 Всего расходов: {expense:.2f}₽")

    markup = create_keyboard()
    bot.send_message(message.chat.id, "Выберите команду:", reply_markup=markup)


# Запуск бота
bot.polling()
