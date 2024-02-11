
import random

def getDiceResult(Input):
    rangeEnd = 9999999999
    
    if Input == 0:
        rangeEnd = 3
    
    if Input == 1:
        rangeEnd = 5
    
    if Input == 2:
        rangeEnd = 7
    
    if Input == 3:
        rangeEnd = 9
    
    if Input == 4:
        rangeEnd = 11
    
    if Input == 5:
        rangeEnd = 13
        
    if Input == 6:
        rangeEnd = 21
        
    result = random.randrange(1 , rangeEnd)
    print(f"Result: {result}")
    print(" ")
    
# Main application
print("Welcome to the Dice Rolling Simulator!")

running = True
while running == True:
    
    print("Please choose a dice you'd like to roll: ")
    print("[0] D2, [1] D4, [2] D6, [3] D8, [4] D10, [5] D12, [6] D20, [7] QUIT")
    
    try:
        userInput = int(input("Option: "))
        
        if userInput >= 0 and userInput <= 7:
            if userInput == 7:
                running = False
                print("Thanks for playing")
            else:
                getDiceResult(userInput)
        else: 
            print("Please input one of the number options.")
            print(" ")
            
    except: 
        print("Please input one of the number options.")
        print(" ")
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
