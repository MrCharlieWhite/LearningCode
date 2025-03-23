# Build a tip calculator where users input the bill amount and the percentage they want to tip.
# The program will calculate and display the total amount to be paid, including the tip.

# Function that will calculate the tip to be added on
def get_tip_value(meal_cost,tip_percentage):
    tip_result = (tip_percentage / 100) * meal_cost + meal_cost
    return tip_result

print("Welcome to the tip calculator!")
while True:
    try:
        meal_cost = float(input(f"Please enter the price of your meal: £"))
    except:
        print("Please enter a valid option.")
        continue

    try:
        tip_percentage = float(input("Please enter the percentage of the meal price you would like to tip: "))
    except:
        print("Please enter a valid option.")
        continue

    print(f"Your meal was £{meal_cost} and you wish to tip {tip_percentage}%")
    confirmation = input("Is this correct, y or n: ")

    if confirmation == "y":
        total_cost = get_tip_value(meal_cost, tip_percentage)
        print(f"Your meal cost £{meal_cost} and you wish to tip {tip_percentage}%, so your total comes to £{total_cost}.")

    elif confirmation == "n":
        print("Please re-enter details")
        continue

    else:
        print("Please choose a valid option")
        continue


