while True:
    print("Engineering Unit Converter")
    print("--------------------------")
    print("1. Milliamps to Amps")
    print("2. Kilo-ohms to Ohms")
    print("3. Millivolts to Volts")
    print("4. Microfarads to Farads")
    print("5. Volts to Millivolts")
    print("6. Exit")
    choice = input("Choose a conversion from 1 to 6: ")

    if choice == "1":
        milliamps = float(input("Enter milliamps: "))
        amps = milliamps / 1000
        print(f"{milliamps} mA = {amps} A")

    elif choice == "2":
        kilo_ohms = float(input("Enter kilo-ohms: "))
        ohms = kilo_ohms * 1000
        print(f"{kilo_ohms} kΩ = {ohms} Ω")

    elif choice == "3":
        millivolts = float(input("Enter millivolts: "))
        volts = millivolts / 1000
        print(f"{millivolts} mV = {volts} V")

    elif choice == "4":
        microfarads = float(input("Enter microfarads: "))
        farads = microfarads / 1_000_000
        print(f"{microfarads} µF = {farads} F")

    elif choice == "5":
        volts = float(input("Enter volts: "))
        millivolts = volts * 1000
        print(f"{volts} V = {millivolts} mV")

    elif choice == "6":
        print("Exiting converter.")
        break
    else:
        print("Invalid choice. Please run the program again and choose 1, 2, 3, 4, 5 or 6.")
    