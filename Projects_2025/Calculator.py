# add, subtract, multiply, divide. functions for each?

def add_calculation(variable_x,variable_y):
    add_result = variable_x + variable_y
    return add_result

def sub_calculation(variable_x,variable_y):
    sub_result = variable_x - variable_y
    return sub_result

def div_calculation(variable_x,variable_y):
    try:
        div_result = variable_x / variable_y
        return div_result
    except ZeroDivisionError as e:
        print("Error: Cannot divide by zero")
        print(f"{e}")
        return "zero_divide"

def mul_calculation(variable_x,variable_y):
    mul_result = variable_x * variable_y
    return mul_result

def get_numbers():
    try:
        variable_x = int(input("Enter first number: "))
        variable_y = int(input("Enter second number: "))
        return variable_x, variable_y
    except:
        print("\nInvalid input. Resetting.")
        return "invalid", "invalid"


print("Welcome to the simple calculator. ")
print("Here are your options: ")
print("(1) Addition")
print("(2) Subtraction")
print("(3) Division")
print("(4) Multiplication")
print("(5) Exit")



while True:
    choice = input("Enter your selected operation [1-5]: ")

    if(choice not in ["1", "2", "3", "4", "5"]):
        print("Please select a valid option")
        continue


    if choice == "1":
        print("\nAddition:")
        variable_x, variable_y = get_numbers()

        if(variable_x == "invalid" or variable_y == "invalid"):
            continue

        add_result = add_calculation(variable_x,variable_y)
        print(f"{variable_x} + {variable_y} = {add_result}")

    if choice == "2":
        print("\nSubtraction:")
        variable_x, variable_y = get_numbers()

        if (variable_x == "invalid" or variable_y == "invalid"):
            continue
        sub_result = sub_calculation(variable_x,variable_y)
        print(f"{variable_x} - {variable_y} = {sub_result}")

    if choice == "3":
        print("\nDivision:")
        variable_x, variable_y = get_numbers()

        if (variable_x == "invalid" or variable_y == "invalid"):
            continue

        div_result = div_calculation(variable_x,variable_y)

        if(div_result == "zero_divide"):
            continue


        print(f"{variable_x} / {variable_y} = {div_result}")

    if choice == "4":
        print("\nMultiplication:")
        variable_x, variable_y = get_numbers()

        if (variable_x == "invalid" or variable_y == "invalid"):
            continue

        mul_result = mul_calculation(variable_x, variable_y)
        print(f"{variable_x} * {variable_y} = {mul_result}")

    if choice == "5":
        print("Thanks for using the basic calculator.")
        break