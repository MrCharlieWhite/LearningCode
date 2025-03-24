import random


def encrypt(x, num_repeats, preferred_encryption_key, original_characters):
    y = list(x)
    z = list(x)
    for i in range(num_repeats):
        for j in range(len(y)):
            for k in range(len(original_characters)):
                if y[j] == original_characters[k]:
                    z[j] = preferred_encryption_key[k]
        y = z
    w = "".join(z)
    return w

def generate_encryption_key(original_characters):
    generated_key = []
    available_characters = original_characters.copy()

    while available_characters:
        random_index = random.randrange(0, len(available_characters))
        generated_key.append(available_characters.pop(random_index))

    return generated_key

def get_number_of_iterations():
    while True:
        try:
            number_of_iterations = int(input("\nEnter desired number of iterations: "))
            if number_of_iterations < 1:
                print("\nNumber of iterations must be greater than 0.\n")
                continue
            return number_of_iterations
        except:
            print("Invalid Number of Iterations. Try Again.")
            continue
def get_encryption_key(user_encryption_choice, original_characters):
    if user_encryption_choice == "1":
        return generate_encryption_key(original_characters)
    else:
        return list("8*1(:9Xm5s^=A/kxzepYhJQ'%yjVNo;&vEIfc2.n7w£,dTWPb60Kt}{ClMG)aZ[3RFrS4+iOgUD$-L!uH]q_B")

def main():
    original_characters = list("1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz;:'.,(){}[]!£$%^&*/+-=_")

    message = input("Type in a message to encrypt: ")

    while True:
        print("\nPress 1 to generate a new encryption key for this encryption.")
        print("Press 2 to use the premade encryption key")
        user_encryption_choice = input("Option: ")

        if user_encryption_choice not in ["1","2"]:
            print("Invalid Input. Try Again.\n")
            continue
        else:
            break

    encryption_key = get_encryption_key(user_encryption_choice, original_characters)
    number_of_iterations = get_number_of_iterations()

    print("Your encrypted result is: " + encrypt(message, number_of_iterations, encryption_key, original_characters))

main()