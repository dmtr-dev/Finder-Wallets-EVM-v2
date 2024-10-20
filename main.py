import pyotp
import time
import pyperclip
from ctypes import windll
from termcolor import cprint

file_path = 'secret_keys.txt'

def read_keys_from_file(file_path):
    keys = {}
    account_names = set()
    with open(file_path, 'r') as file:
        for line in file:
            if ':' in line:
                account_name, secret_key = line.strip().split(':')
                lower_account_name = account_name.lower()
                
                if lower_account_name in account_names:
                    print(f"Ошибка: дублирующееся название '{account_name}'. Пожалуйста, измените его в файле.")
                    return None
                if lower_account_name == "exit":
                    print(f"Ошибка: недопустимое название '{account_name}'. Пожалуйста, измените его в файле.")
                    return None
                
                keys[lower_account_name] = secret_key
                account_names.add(lower_account_name)
    return keys

keys = read_keys_from_file(file_path)

if keys is None:
    exit()

while True:
    account_name = input("Введите название аккаунта (или 'exit' для выхода): ").lower()
    
    if account_name == 'exit':
        print("Выход из программы.")
        break
    
    if account_name in keys:
        secret_key = keys[account_name]
        totp = pyotp.TOTP(secret_key, interval=30)

        otp_code = totp.now()

        remaining_time = 30 - (int(time.time()) % 30)

        pyperclip.copy(otp_code)

        print(f"Код для '{account_name}': {otp_code} (действителен еще {remaining_time} секунд)\n")
    else:
        print("Такого аккаунта нет. Попробуйте снова.\n")

if __name__ == "__main__":
    windll.kernel32.SetConsoleTitleW('Finder Wallets EVM | by https://t.me/dmtrcrypto')
    cprint("\nTG Channel - https://t.me/dmtrcrypto\n\n", 'magenta')
