while 0 < 1:
    def calculate_specific_resistance(R, A, l):

        rho = R * (A / l)
        return rho


    R = float(input("Введите сопротивление проводника (в Омах): "))
    A = float(input("Введите площадь поперечного сечения проводника (в м²): "))
    l = float(input("Введите длину проводника (в метрах): "))
    if R < 0:
        print("Сопротивление меньше нуля.")
    if A < 0:
        print("Площадь поперечного сечения не может быть < 0")
    if l < 0:
        print("Длина не может быть < 0")
    rho = calculate_specific_resistance(R, A, l)
    print(f"Удельное сопротивление проводника: {rho} Ом*м")
