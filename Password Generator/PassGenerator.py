import time
import secrets
import json

# Load configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

spc = '--------------'

currentVersion = 'v1.1'

# Character sets
charsAll = config['charsAll']
charsNum = config['charsNum']
charsLet = config['charsLet']
charsLoB = config['charsLoB']
charsLoS = config['charsLoS']
charsSpe = config['charsSpe']

# Dictionary to map typeChar options to character sets
char_sets = {
    'all': charsAll,
    'numbers': charsNum,
    'letters': charsLet,
    'onlySmallLetters': charsLoS,
    'onlyCapsLetters': charsLoB,
    'special': charsSpe
}

def get_user_input():
    while True:
        typeChar = input('Select character range from the following options: (all / numbers / special / letters / onlySmallLetters / onlyCapsLetters): ')
        if typeChar in char_sets:
            break
        else:
            print('Invalid option. Please enter a valid option.')
    
    while True:
        try:
            length = int(input('Length to add? (Starts at 0) :'))
            if length > 0:
                break
            else:
                print('Length must be a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a valid integer.')
    
    return typeChar, length

def generate_password(chars, length):
    password = ''
    for _ in range(length):
        password += secrets.choice(chars)
    return password

def check_password_strength(password):
    length_criteria = len(password) >= 8
    upper_criteria = any(c.isupper() for c in password)
    lower_criteria = any(c.islower() for c in password)
    digit_criteria = any(c.isdigit() for c in password)
    special_criteria = any(c in charsSpe for c in password)
    
    score = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])
    
    if score == 5:
        return 'Strong'
    elif score >= 3:
        return 'Medium'
    else:
        return 'Weak'

def save_password_to_file(password):
    with open('password.txt', 'w') as file:
        file.write(password)
    print('Password saved to password.txt')

def main():
    print('OJAVE CONSOLE-BASED-SOFTWARE LIMITED')
    print('< Loading Application >')
    print()
    time.sleep(1)
    print('Version:', currentVersion)
    print()
    time.sleep(1)
    
    while True:
        typeChar, length = get_user_input()
        chars = char_sets[typeChar]
        password = generate_password(chars, length)
        
        print(spc)
        print(password)
        print('Password strength:', check_password_strength(password))
        print(spc)
        
        save_option = input('Save password to file? (y/n): ')
        if save_option == 'y':
            save_password_to_file(password)
        
        close_option = input('Close? (y/n): ')
        if close_option == 'y':
            print('Goodbye')
            time.sleep(1)
            raise SystemExit(0)
        print(spc)

if __name__ == '__main__':
    main()
