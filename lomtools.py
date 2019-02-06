#Import Modules
import os, time, webbrowser, pyperclip;

print("          |_____________________________________________________________|")
print("          |=============================================================|")
print("                                  Hello in LOMTOOLS                      ")
print("                               Programing by ONEALONER                   ")
print("          |=============================================================|")
print("          |_____________________________________________________________|")

while True:
    mode = int(input("\n                 |---| 1) Caesar cipher  2) IP Local |--|\n                 |---| 3) #  4) Close  |--|\n                 |---| > "))
    if mode == 1:
        while True:
            os.system('CLS')
            mode1 = int(input("\n                 |---| 1) Code 2) Decode 3) Close\n                 |---| > "))
            if mode1 == 1:
                os.system('CLS')
                alpha = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=+?!'
                n = int(input("\n                 |---| Write numder:\n                 |---| > "))
                os.system('CLS')
                s = input("\n                 |---| Write text:\n                 |---| > ").strip()
                os.system('CLS')
                res = ''
                for c in s:
                    res += alpha[(alpha.index(c) + n) % len(alpha)]
                os.system('CLS')
                print('\n                 |---| Result: "' + res + '"')
                time.sleep(20)
                break
            elif mode1 == 2:
                os.system('CLS')
                alpha = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=+?!'
                n = int('-' + input("\n                 |---| Write numder:\n                 |---| > "))
                os.system('CLS')
                s = input("\n                 |---| Write text:\n                 |---| > ").strip()
                res = ''
                for c in s:
                    res += alpha[(alpha.index(c) + n) % len(alpha)]
                os.system('CLS')
                print('\n                 |---| Result: "' + res + '"')
                time.sleep(20)
                break
            elif mode1 == 3:
                break
            else:
                print("\n                 |---| Write INT namber please!!!")
                time.sleep(20)
                break
    elif mode == 2:
         os.system('CLS')
         ip = input ("\n                 |---| IP adress: ")
         time.sleep(4)
         webbrowser.open('https://ru.infobyip.com/ip-'+ ip +'.html')
    elif mode == 4:
        break
    else:
        pass
