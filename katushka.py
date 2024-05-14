import math
while 0 < 1:
    print("Пока что тут можно расчитать индуктивность плоской катушки.")
    def calculate_inductance(N, r, l):
        mu0 = 4 * math.pi * 10**-7  # Магнитная постоянная в Гн/м
        A = math.pi * r**2  # Площадь поперечного сечения катушки в м^2
        L = (N**2 * mu0 * A) / l  # Расчет индуктивности
        return L

    N = float(input("количество витков:"))  
    r = float(input("радиус катушки в метрах:"))  
    l = float(input("длина катушки в метрах:")) 
    if N < 0:
        print("Колличество витков не может быть = 0")
    if r < 0:
        print("Радиус не может быть < 0")
    if l < 0:
        print("Длина не может быть < 0")
    
    inductance = calculate_inductance(N, r, l)
    print(f"Индуктивность катушки: {inductance} Генри")
