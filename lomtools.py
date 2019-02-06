#Import Modules
import os, time, webbrowser, pyperclip;

print("          |_____________________________________________________________|")
print("          |=============================================================|")
print("                                  Hello in LOMTOOLS                      ")
print("                                Programing by UNIT80                     ")
print("                                    FREE VERSION                         ")
print("          |=============================================================|")
print("          |_____________________________________________________________|")

while True:
    mode = int(input("\n                 |---| 1) Caesar cipher  2) IP Local |--|\n                 |---| 3) IP LOGGER  4) BSSID Local  |--|\n                 |---| 5) IP (View downloads)  6) Close  |--|\n                 |---| > "))
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
                time.sleep(10)
                os.system('CLS')
                pass
    elif mode == 2:
         os.system('CLS')
         ip = input ("\n                 |---| IP adress: ")
         time.sleep(4)
         webbrowser.open('https://ru.infobyip.com/ip-'+ ip +'.html')
         os.system('CLS')
    elif mode == 3:
        os.system('CLS')
        pyperclip.copy('https://2no.co/1pnm37.js')
        print("\n                 |---| Link copied: https://2no.co/1pnm37.js")
        time.sleep(4)
        webbrowser.open("http://iplogger.ru/logger/67aktn1pnm37/")
        os.system('CLS')
    elif mode == 4:
         os.system('CLS')
         bssid = input ("\n                 |---| BSSID: ")
         time.sleep(2)
         webbrowser.open('http://api.mylnikov.org/geolocation/wifi?bssid='+ bssid)
         os.system('CLS')
    elif mode == 5:
         os.system('CLS')
         torrent = input ("\n                 |---| IP adress: ")
         time.sleep(4)
         webbrowser.open('https://iknowwhatyoudownload.com/ru/peer/?ip='+ torrent)
    elif mode == 6:
        break
    else:
        pass
