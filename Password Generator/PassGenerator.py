import time
import random
import webbrowser

spc = '--------------'
password = ''

currentVersion = 'v1.0'

charsAll = 'abcdefghijklmopqrstuvewd1234567890!@#$%^&*()-=QWERTYUIOPASDFGHJKLZXCVBNM,./;l]['
charsNum = '123456789'
charsLet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
charsLoB = 'QWERTYUIOPASDFGHJKLZXCVBNM'
charsLoS = 'qwertyuiopasdfghjklzxcvbnm'
charsSpe = '!@#$%^&*(_+)><":~|}{":?><'

print('OJAVE CONSOLE-BASED-SOFTWARE LIMITED')
print('< Loading Application >')
print()
time.sleep(1)
print('Version:', currentVersion)
print()
time.sleep(1)
bronfirmCheck = 20
while bronfirmCheck == 20:           
    typeChar = input('Select character range from the following options: (all / numbers / special / letters / onlySmallLetters / onlyCapsLetters): ')
    if typeChar == 'letters':
        chars = charsLet
    if typeChar == 'all':
        chars = charsAll
    if typeChar == 'numbers':
        chars = charsNum
    if typeChar == 'special':
        chars = charsSpe
    if typeChar == 'onlySmallLetters':
        chars = charsLoS
    if typeChar == 'onlyCapsLetters':
        chars = charsLoB
    confirmCheck = 10

    while confirmCheck == 10:
        length = input('Length to add? (Starts at 0) :')
        length = int(length)
        print(spc)
        for c in range(length):
            password += random.choice(chars)
        print(password)
        time.sleep(0.5)
        print(spc)
        CONA = input('Close? (y/n): ')
        if CONA == 'y':
            print('Goodbye')
            time.sleep(1)
            raise SystemExit(0)
        if CONA == 'n':
            confirmCheck + 0
        print(spc)
           