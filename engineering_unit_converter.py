def show_menu():
    print("Engineering Unit Converter")
    print("--------------------------")
    print("1. Milliamps to Amps")
    print("2. Kilo-ohms to Ohms")
    print("3. Millivolts to Volts")
    print("4. Microfarads to Farads")
    print("5. Volts to Millivolts")
    print("6. Exit")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a valid number.")


while True:
    show_menu()
    choice = input("Choose an option from 1 to 6: ")

    if choice == "1":
        milliamps = get_number("Enter milliamps: ")
        amps = milliamps / 1000
        print(f"{milliamps:,.2f} mA = {amps:,.2f} A")

    elif choice == "2":
        kilo_ohms = get_number("Enter kilo-ohms: ")
        ohms = kilo_ohms * 1000
        print(f"{kilo_ohms:,.2f} kΩ = {ohms:,.2f} Ω")

    elif choice == "3":
        millivolts = get_number("Enter millivolts: ")
        volts = millivolts / 1000
        print(f"{millivolts:,.2f} mV = {volts:,.2f} V")

    elif choice == "4":
        microfarads = get_number("Enter microfarads: ")
        farads = microfarads / 1_000_000
        print(f"{microfarads:,.2f} µF = {farads:,.2f} F")

    elif choice == "5":
        volts = get_number("Enter volts: ")
        millivolts = volts * 1000
        print(f"{volts:,.2f} V = {millivolts:,.2f} mV")

    elif choice == "6":
        print("Exiting converter.")
        break
    else:
        print("Invalid option. Please choose 1, 2, 3, 4, 5, or 6.")    