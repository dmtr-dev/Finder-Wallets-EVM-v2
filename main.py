from eth_account import Account
from ctypes import windll

windll.kernel32.SetConsoleTitleW('Finder Wallets EVM | by https://t.me/dmtrcrypto')
print("\n\033[94mTG Channel Creator - https://t.me/dmtrcrypto\033[0m\n\n")


target = input("Enter the sequence of characters: ").lower()
count = int(input("Enter the number of wallets: "))
while True:
    position = input("Enter which side of the wallet address should contain the characters (s - start, e - end): ").lower()
    if position in ['s', 'e']:
        break
    else:
        print("Invalid input. Please enter 's' for start or 'e' for end")

def create_wallets(target, count, position, num_words=12):
    Account.enable_unaudited_hdwallet_features()
    wallets = []

    for _ in range(count):
        while True:
            account, mnemonic = Account.create_with_mnemonic(num_words=num_words)
            
            if is_valid_address(account.address[2:], target, position):
                wallets_info = f'{account.address}:{mnemonic}:{account.key.hex()}'
                wallets.append(wallets_info)
                print(f"Found valid wallet: {account.address}")
                break
    
    with open(f'wallets_{target}.txt', 'w') as file:
        file.write("address : mnemonic : private_key\n\n")
        for wallet in wallets:
            file.write(wallet + '\n')
    print(f"\nValid wallets have been written to 'wallets_{target}.txt'")

def is_valid_address(address, target, position):
    if position == 's':
        return address.startswith(target)
    elif position == 'e':
        return address.endswith(target)
    return False

if __name__ == "__main__":
    create_wallets(target, count, position)