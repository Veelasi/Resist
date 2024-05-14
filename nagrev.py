while 0 < 1:
    print("####################")
    print("Температурный коэф. сопротивления (1/°C)")
    print("1. Медь: 0.00386 (°C^-1)")
    print("2. Алюминий: 0.0039 (°C^-1)")
    print("3. Свинец: 0.0039 (°C^-1)")
    print("4. Никель: 0.00617 (°C^-1)")
    print("5. Железо: 0.005 (°C^-1)")
    print("####################")
    print("Удельное сопротивление при 20°C")
    print("- Медь (Cu): \(1,68 \times 10^{-8}\) Ом·м")
    print("- Алюминий (Al): \(2,82 \times 10^{-8}\) Ом·м")
    print("- Свинец (Pb): \(2,2 \times 10^{-7}\) Ом·м")
    print("- Никель (Ni): \(6,99 \times 10^{-8}\) Ом·м")
    print("- Железо (Fe): \(9,71 \times 10^{-8}\) Ом·м")
    def calculate_resistivity(rho0, alpha, T, T0=293):

        rho = rho0 * (1 + alpha * (T - T0))
        return rho


    rho0 = float(input(" Удельное сопротивление при 20°C (Ом*м):"))
    alpha = float(input("Температурный коэффициент сопротивления (1/°C):"))
    T_current = float(input("Текущая температура в Кельвинах:"))

    rho = calculate_resistivity(rho0, alpha, T_current)
    print(f"Удельное сопротивление проводника при {T_current} K: {rho} Ом*м")

