import languages
import config
from coder import encrypt, decrypt
import telebot
from telebot import types
import json


TOKEN = config.TOKEN
DATA_FILE = "users.json"

bot = telebot.TeleBot(TOKEN)


def open_bot_menu(message):
    user_id = str(message.from_user.id)
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        buttons_text = languages.menu_buttons_text(data[user_id]["language"])
        menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu_markup.row(types.KeyboardButton(buttons_text[0]), types.KeyboardButton(buttons_text[1]))
        menu_markup.row(types.KeyboardButton(buttons_text[2]))
        bot.send_message(message.chat.id, languages.menu_text(data[user_id]["language"]), reply_markup=menu_markup)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = str(message.from_user.id)
    with open(DATA_FILE, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        if user_id not in data:
            data[user_id] = {"language": "eng", "coder_version": "v0.1", "last_text": ""}
            f.seek(0)
            json.dump(data, f, indent=4, ensure_ascii=False)
            f.truncate()
        bot.send_message(message.chat.id, languages.start_text(data[str(message.from_user.id)]["language"]))
        open_bot_menu(message)

@bot.message_handler(commands=['menu'])
def menu(message):
    open_bot_menu(message)



@bot.message_handler(func=lambda message: message.text in ["Зашифровать", "Encode"])
def encode_part_one(message):
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        text = languages.encode_text(data[str(message.from_user.id)]["language"])
        bot.send_message(message.chat.id, text[0], reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, encode_part_two)

def encode_part_two(message):
    with open(DATA_FILE, 'r+', encoding='utf-8') as f:
        data = json.load(f)

        data[str(message.from_user.id)]["last_text"] = message.text

        text = languages.encode_text(data[str(message.from_user.id)]["language"])
        bot.send_message(message.chat.id, text[1])

        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()

        bot.register_next_step_handler(message, encode_part_three)

def encode_part_three(message):
    if message.text[0] != '/':
        with open(DATA_FILE, 'r+', encoding='utf-8') as f:
            data = json.load(f)

            try:
                n = int(message.text)
                crypted_text = encrypt(data[str(message.from_user.id)]["last_text"], n)
                data[str(message.from_user.id)]["last_text"] = ""
                text = languages.encode_text(data[str(message.from_user.id)]["language"])

                f.seek(0)
                json.dump(data, f, indent=4, ensure_ascii=False)
                f.truncate()

                bot.send_message(message.chat.id, f"{text[2]}\n`{crypted_text}`", parse_mode="MARKDOWN")
                open_bot_menu(message)
            except:
                bot.send_message(message.chat.id, languages.encode_error1_text(data[str(message.from_user.id)]["language"]))
                bot.register_next_step_handler(message, encode_part_three)

@bot.message_handler(func=lambda message: message.text in ["Расшифровать", "Decode"])
def decode_part_one(message):
    with open(DATA_FILE, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        text = languages.decode_text(data[str(message.from_user.id)]["language"])
        bot.send_message(message.chat.id, text[0], reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, decode_part_two)

def decode_part_two(message):
    with open(DATA_FILE, 'r+', encoding='utf-8') as f:
        data = json.load(f)

        data[str(message.from_user.id)]["last_text"] = message.text

        text = languages.decode_text(data[str(message.from_user.id)]["language"])
        bot.send_message(message.chat.id, text[1])

        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()

        bot.register_next_step_handler(message, decode_part_three)

def decode_part_three(message):
    with open(DATA_FILE, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        try:
            crypted_text = decrypt(data[str(message.from_user.id)]["last_text"], int(message.text))
            if crypted_text == None:
                bot.send_message(message.chat.id, languages.decode_error1_text(data[str(message.from_user.id)]["language"]))
                bot.register_next_step_handler(message, decode_part_three)
            elif crypted_text == "Error string":
                bot.send_message(message.chat.id, languages.decode_error2_text(data[str(message.from_user.id)]["language"]))
                bot.register_next_step_handler(message, decode_part_two)
            else:
                data[str(message.from_user.id)]["last_text"] = ""
                text = languages.decode_text(data[str(message.from_user.id)]["language"])
                f.seek(0)
                json.dump(data, f, indent=4, ensure_ascii=False)
                f.truncate()
                bot.send_message(message.chat.id, f"{text[2]}\n`{crypted_text}`", parse_mode="MARKDOWN")
                open_bot_menu(message)
        except:
            bot.send_message(message.chat.id, languages.decode_error3_text(data[str(message.from_user.id)]["language"]))
            bot.register_next_step_handler(message, decode_part_three)

@bot.message_handler(commands=['settings'])
@bot.message_handler(func=lambda message: message.text in ["Настройки", "Settings"])
def open_bot_settings(message):
    user_id = str(message.from_user.id)
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        text = languages.settings_button_text(data[user_id]["language"])
        settings_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        settings_markup.row(types.KeyboardButton(text[0]))
        settings_markup.row(types.KeyboardButton(text[1]))
        bot.send_message(message.chat.id, languages.settings_text(data[user_id]["language"])+data[user_id]["coder_version"], reply_markup=settings_markup)

@bot.message_handler(func=lambda message: message.text in ["Изменить язык", "Change language"])
def change_language_part_one(message):
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        languages_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        languages_markup.row(types.KeyboardButton("ru"), types.KeyboardButton("eng"))
        bot.send_message(message.chat.id, languages.change_language_text(data[str(message.from_user.id)]["language"]), reply_markup=languages_markup)
        bot.register_next_step_handler(message, change_language_part_two)

def change_language_part_two(message):
    user_id = str(message.from_user.id)
    with open(DATA_FILE, 'r+', encoding='utf-8') as f:
        data = json.load(f)
        data[user_id]["language"] = message.text
        text = languages.settings_button_text(data[user_id]["language"])
        settings_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        settings_markup.row(types.KeyboardButton(text[0]))
        settings_markup.row(types.KeyboardButton(text[1]))
        text = languages.settings_text(data[user_id]["language"])+data[user_id]["coder_version"]
        f.seek(0)
        json.dump(data, f, indent=4, ensure_ascii=False)
        f.truncate()
        bot.send_message(message.chat.id, text, reply_markup=settings_markup)

@bot.message_handler(func=lambda message: message.text in ["Изменить версию шифратора", "Change version of encoder"])
def change_version_of_encoder(message):
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
        bot.send_message(message.chat.id, languages.change_version_of_encoder_text(data[str(message.from_user.id)]["language"]))
        open_bot_menu(message)


if __name__ == '__main__':
    bot.polling(non_stop=True)
    print("Бот запущен...")