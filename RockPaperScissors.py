import random
print("Welcome to Rock, Paper, Scissors!")

#Functions
def getChoice(option): 
    if option == 1: 
        return "Rock"
    if option == 2: 
        return "Paper"
    if option == 3: 
        return "Scissors"
    else: 
        raise Exception("Invalid choice.")
        
def getBotInput():
    botResponse = random.randint(1,3) # 1
    return botResponse # 1

def getWinner(userChoice, botChoice): 
    if userChoice == botChoice: 
        return "Tie"
    if userChoice == "Rock" and botChoice == "Scissors":
        return "User"
    if userChoice == "Scissors" and botChoice == "Paper":
        return "User"
    if userChoice == "Paper" and botChoice == "Rock":
        return "User"
    else:
        return "Bot"

def rockPaperScissorsGame(): 
    running = True
    while running == True:
        print("Please select a number: [1] Rock, [2] Paper, [3] Scissors, [0] QUIT")
    
        try:
            # Get user numeric input
            userInput = int(input("Option: "))
            if userInput == 0:
                running = False
                print("Goodbye (your family has been [REDACTED])")
                return 0
            
            # Get bot numeric input
            botInput = getBotInput()
            
            # Get options as strings
            userOption = getChoice(userInput)
            botOption = getChoice(botInput)
            
            winner = getWinner(userOption,botOption)
            print(f"You chose: {userOption}. The bot chose: {botOption}. The winner is: {winner}")        
        except ValueError:
            print("Choose a number you [REDACTED].")
        except Exception as error: 
            print(error)
            
rockPaperScissorsGame()
        
