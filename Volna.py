import math
while 0 < 1:
    def calculate_frequency(wave_length, speed_of_sound):
        frequency = speed_of_sound / wave_length
        return frequency

    wave_length = float(input("Введите длину волны (в метрах): "))
    speed_of_sound = float(input("Введите скорость звука (в м/с): "))
    if wave_length < 0:
         print("Ты у длины отрицательное значение указал")
    if speed_of_sound < 0:
         print("Скорость не может быть отрицательной.")
    result_frequency = calculate_frequency(wave_length, speed_of_sound)
    print("Частота звука равна", result_frequency, "Гц")
