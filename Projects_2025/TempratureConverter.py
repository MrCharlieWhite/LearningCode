# Fahrenheit  to Celsius (f − 32) × 5/9 = c
# Celsius to Fahrenheit  (c × 9/5) + 32 = f

def fahrenheit_to_celsius(f_temp):
    c_temp = (f_temp - 32) * (5/9)
    return c_temp

def celsius_to_fahrenheit(c_temp):
    f_temp = (c_temp * 9/5) + 32
    return f_temp

def get_user_temperature_choice(temp_type):
    try:
        return int(input(f"Please enter the {temp_type} temperature you would like to convert: "))
    except:
        print("Invalid temperature, please try again")
        return "invalid"

print("Welcome to the Temperature Converter")
print("Here are your options:")
print("1. Fahrenheit to Celsius")
print("2. Celsius to Fahrenheit")
print("3. Quit")


while True:
    # Take operation input
    choice = input("\nEnter operation number (1-3): ")

    # Check if user wants to exit
    if choice == '3':
        print("Thank you for using the converter. Goodbye!")
        break

    if choice not in ['1', '2', '3']:
        print("Invalid choice. Please select another option")
        continue

    if choice == "1":
        fahrenheit_temp = get_user_temperature_choice("fahrenheit (°F)")

        if(fahrenheit_temp == "invalid"):
            continue

        celsius_temp = fahrenheit_to_celsius(fahrenheit_temp)
        print(f"{fahrenheit_temp}°F in celsius is: {int(celsius_temp)}°C")
    elif choice == "2":
        celsius_temp = get_user_temperature_choice("celsius (°C)")

        if(celsius_temp == "invalid"):
            continue

        fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
        print(f"{celsius_temp}°C in fahrenheit is: {int(fahrenheit_temp)}°F")


