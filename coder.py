import random

ALL_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~"

def init_group_of_symbols(seed):
    """Распределяет символы по 4 строкам"""
    SYMBOLS_GROUP = ['', '', '', '']
    rng = random.Random(seed)
    for symbol in ALL_SYMBOLS:
        SYMBOLS_GROUP[rng.randint(0, 3)] += symbol
    return SYMBOLS_GROUP

def generate_mask(seed, length):
    """Генерирует битовую маску заданной длины с фиксированным seed."""
    rng = random.Random(seed)
    return ''.join(rng.choice('01') for _ in range(length))

def encrypt(text, n):
    """Шифрует строку с использованием маски силы n."""
    if not text:
        return ""
    
    # Преобразование текста в биты
    bytes_data = text.encode('utf-8')
    bits = ''.join(f"{byte:08b}" for byte in bytes_data)
    L = len(bits)
    
    # Генерация маски и применение XOR
    mask = generate_mask(n, L)
    masked_bits = ''.join('1' if b != m else '0' for b, m in zip(bits, mask))
    
    # Разбиение на пары бит и замена символами
    SYMBOLS_GROUP = init_group_of_symbols(n)
    pairs = [masked_bits[i:i+2] for i in range(0, L, 2)]
    char_sets = {'00': SYMBOLS_GROUP[0], '01': SYMBOLS_GROUP[1], '10': SYMBOLS_GROUP[2], '11': SYMBOLS_GROUP[3]}
    return ''.join(random.choice(char_sets[pair]) for pair in pairs)

def decrypt(cipher_text, n):
    """Дешифрует строку, используя маску силы n."""
    if not cipher_text:
        return ""
    
    # Преобразование символов в биты
    SYMBOLS_GROUP = init_group_of_symbols(n)
    bits_list = []
    for char in cipher_text:
        if char in SYMBOLS_GROUP[0]:
            bits_list.append('00')
        elif char in SYMBOLS_GROUP[1]:
            bits_list.append('01')
        elif char in SYMBOLS_GROUP[2]:
            bits_list.append('10')
        elif char in SYMBOLS_GROUP[3]:
            bits_list.append('11')
        else:
            return "Error string"
    bits = ''.join(bits_list)
    L = len(bits)
    
    # Генерация маски и применение XOR
    mask = generate_mask(n, L)
    original_bits = ''.join('1' if b != m else '0' for b, m in zip(bits, mask))
    
    # Преобразование битов в строку
    byte_array = bytearray()
    for i in range(0, len(original_bits), 8):
        byte_bits = original_bits[i:i+8]
        byte_array.append(int(byte_bits, 2))
    try:
        return byte_array.decode('utf-8')
    except:
        return None

if __name__ == '__main__':
    while True:
        mode = int(input("\033[1mВыберите что вы хотите сделать:\033[0m\n0 - Зашифровать строку\n1 - Расшифровать строку\n2 - Завершить выполнение программы\n>>> \033[32m"))
        if not mode:
            user_input = input("\033[0m\nВведите строку:\n>>> \033[32m")
            seed = int(input("\033[0mВведите код для шифрования:\n>>> \033[32m"))
            print(f"\033[0m\033[1m\nЗашифрованная строка:\033[0m\033[33m\n{encrypt(user_input, seed)}\033[0m\n")
        elif mode == 1:
            user_input = input("\033[0m\nВведите строку:\n>>> \033[32m")
            seed = int(input("\033[0mВведите код для расшифрования:\n>>> \033[32m"))
            output = decrypt(user_input, seed)
            if output != None:
                print(f"\033[0m\033[1m\nРасшифрованная строка:\033[0m\033[33m\n{output}\033[0m\n")
            else:
                print("\n\033[31m\033[1mОшибка\033[0m\nВозможно вы ввели неправильный код\n")
        else:
            print("\033[0m")
            break