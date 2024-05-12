AMPER = int(2)
while 0 < 1:
    print("ResistV1")
    print("Расчет сопротивления резистора для светодиода")
    print("Параллельное - 1; Последовательное - 2; Настройки - 3;")
    a = int(input())
    if a == 1:
        print("Источник напряжения? (В)")
        U = input()
        U = float(U)
        print("Падение напряжения светодиода? (В)")
        U2 = input()
        U2 = float(U2)
        if AMPER == 2:
            print("Ток потребления светодиода? (А)")
        if AMPER == 1:
            print("Ток потребления светодиода? (mA)")
        I = input()
        I = float(I)
        if AMPER == 1:
            I = float(I*1000)
            R = (U - U2)/I
        if AMPER == 2:
            R = (U - U2)/I
        print("")
        print("Сопротивление резистора:")
        print(R, "Ом;")
        print("")
        print("Требуемая мощность резистора:")
        print((I*I)*R, "Вт;")
        print("")
        print("Мощность в цепи:")
        print(I*U, "Вт;")
        print("")
    if a == 2:
        print("Источник напряжения? (В)")
        U = input()
        U = float(U)
        print("Падение напряжения светодиода? (В)")
        U2 = input()
        U2 = float(U2)
        print("Количество светодиодов в цепи?")
        Round = input()
        Round = float(Round)
        if Round % 1 != 0:
            print("Чумба, ты совсем ебнутый? Половина светодиода работать не будет.")
            print("Лады, считаем дальше")
        if AMPER == 1:
            print("Ток потребления светодиода? (mА)")
        if AMPER == 2:
            print("Ток потребления светодиода? (А)")
        I = input()
        I = float(I)
        if AMPER == 1:
            I = float(I*1000)
            R = (U-(U2*Round))/I
        if AMPER == 2:
            R = (U-(U2*Round))/I
        if U < Round*U2:
            print("Работать не будет. Сумма падений напряжений больше, чем источник питания")
        print("")
        print("Сопротивление резистора:")
        print(R, "Ом;")
        print("")
        print("Требуемая мощность резистора:")
        print((I*I)*R, "Вт;")
        print("")
        print("Мощность в цепи:")
        print(I*U, "Вт;")
        print("")
    if a == 3:
        print("Пока тут можно изменить еденицы измерения силы тока")
        print("с ампер на милли амперы. Пук-пук")
        print("Брать показания в милли амперах - 1;")
        print("Брать показания в амперах - 2;")
        AMPER = int(input())
