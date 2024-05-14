import os
#os.startfile(r'C:\Rproject\ResistV1.py')
while 0 < 1:
    print("Rproject.inc")
    print("Что будем считать?")
    print("1 - Сопротивление резистора для светодиода")
    print("2 - Частота колебательного контура")
    print("3 - Расчет частоты исходя из волны")
    print("4 - Индуктивность катушки по намотанный данным")
    print("5 - Удельное сопротивление проводника")
    print("6 - Удельное сопротивление проводника по нагреву (< 200 C)")
    a = int(input())
    if a == 1:
        os.startfile(r'C:\Rproject\ResistV1.py')
    if a == 2:
        os.startfile(r'C:\Rproject\Chastota.py')
    if a == 3:
        os.startfile(r'C:\Rproject\Volna.py')
    if a == 4:
        os.startfile(r'C:\Rproject\katushka.py')
    if a == 5:
        os.startfile(r'C:\Rproject\udelnoe.py')
    if a == 6:
        os.startfile(r'C:\Rproject\nagrev.py')
    else:
        print("В диапазоне чисел выше укажи число")
