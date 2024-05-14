import math
while 0 < 1:
    def thomson_formula(L, C):
        omega = 1 / math.sqrt(L * C)
        f = omega / (2 * math.pi)
        return omega, f

    # ввод значений индуктивности и ёмкости
    L = float(input("Введите индуктивность (Гн): "))
    C = float(input("Введите ёмкость (Ф): "))
    if L < 0:
        print("Индуктивность не может быть меньше нуля.")
    if C < 0:
        print("Отрицательную емкость еще не придумали.")
    # расчет по формуле Томсона
    omega, f = thomson_formula(L, C)

    # вывод результатов
    print(f"Частота колебаний (f): {f} Гц")
    print(f"Угловая частота (omega): {omega} рад/с")
