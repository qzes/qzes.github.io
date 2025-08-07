def start_text(language="ru"):
    if language == "ru":
        return "Добро пожаловать в @qzes_coder_bot\n\nМы предлагаем услуги по шифрованию и расшифрованию текста с использованием кодов шифрования.\nВсе алгоритмы полностью разработаны нами, исходный код нигде на распространяется, мы не храним данные о ваших действиях в боте (кроме настроек), что обеспечивает полную безопасность ваших личных данных"
    elif language == "eng":
        return "Welcome to @qzes_coder_bot\n\nWe offer text encryption and decryption services using encryption codes.\nAll algorithms are fully developed by us, the source code is not distributed anywhere, we do not store data about your actions in the bot (except for settings), which ensures the complete security of your personal data"
    

def menu_text(language="ru"):
    if language == "ru":
        return "Открываю главное меню"
    elif language == "eng":
        return "Open main menu"
    

def menu_buttons_text(language="ru"):
    if language == "ru":
        return ["Зашифровать", "Расшифровать", "Настройки"]
    elif language == "eng":
        return ["Encode", "Decode", "Settings"]
    

def encode_text(language="ru"):
    if language == "ru":
        return ["Введите текст", "Введите код шифрования", "Зашифрованный текст: "]
    elif language == "eng":
        return ["Type your text", "Write code", "Encrypted text: "]
    

def decode_text(language="ru"):
    if language == "ru":
        return ["Введите зашифрованный текст", "Введите код шифрования", "Расшифрованный текст: "]
    elif language == "eng":
        return ["Type your text for decode", "Write code", "Decrypted text: "]
    

def encode_error1_text(language="ru"):
    if language == "ru":
        return "Ошибка шифрования!\nКод шифрования может состоять только из символов 0123456789 проверьте код ещё раз\n\nПопробуйте ввести код ещё раз или вернитесь в меню спомощью /menu"
    elif language == "eng":
        return "Encode error!\nThe encryption code can only consist of characters 0123456789 check the code again\n\nTry to enter the code again or return to the menu using /menu"


def decode_error1_text(language="ru"):
    if language == "ru":
        return "Ошибка расшифровки!\nВозможно вы ввели неправильный код шифрования\n\nПопробуйте ввести код ещё раз или вернитесь в меню спомощью /menu"
    elif language == "eng":
        return "Decode error!\nMaybe you write wrong encryption code\n\nTry to enter the code again or return to the menu using /menu"
    

def decode_error2_text(language="ru"):
    if language == "ru":
        return "Ошибка расшифровки!\nВ строке которую вы ввели встретился неизвестный символ проверьте строку\n\nПопробуйте ввести строку ещё раз или вернитесь в меню спомощью /menu"
    elif language == "eng":
        return "Decode error!\nThere is an unknown character in the string you entered, check the string\n\nTry to write string again or return to the menu using /menu"


def decode_error3_text(language="ru"):
    if language == "ru":
        return "Ошибка расшифровки!\nКод шифрования может состоять только из символов 0123456789 проверьте код ещё раз\n\nПопробуйте ввести код ещё раз или вернитесь в меню спомощью /menu"
    elif language == "eng":
        return "Decode error!\nThe encryption code can only consist of characters 0123456789 check the code again\n\nTry to enter the code again or return to the menu using /menu"


def settings_text(language="ru"):
    if language == "ru":
        return "Настройки\nВернуться в меню: /menu\n\nЯзык: РУССКИЙ(ru)\nВерсия шифратора: "
    elif language == "eng":
        return "Settings\nBack to menu: /menu\n\nLanguage: ENGLISH(eng)\nCoder version: "
    

def settings_button_text(language="ru"):
    if language == "ru":
        return ["Изменить язык", "Изменить версию шифратора"]
    elif language == "eng":
        return ["Change language", "Change version of encoder"]
    

def change_language_text(language="ru"):
    if language == "ru":
        return "Изменение языка\n\nВыберите язык из предложенных"
    elif language == "eng":
        return "Change language\n\nChoose language from list"
    

def change_version_of_encoder_text(language="ru"):
    if language == "ru":
        return "Изменение версии шифратора пока недоступно\n\nДобавим в будующих обновлениях"
    elif language == "eng":
        return "Changing the version of the encoder is not yet available\n\nWe will add it in future updates"