import random 

def getQuestionNumbers(): 
    num1 = random.randrange(0,10)
    num2 = random.randrange(0,10)
    answer = num1 + num2
    return num1, num2, answer
    
def getUserAnswer(rn1, rn2):
    userResponse = int(input(f"Please answer this {rn1} + {rn2}: ")) 
    return userResponse

def printResult(userAnswer,questionAnswer ):
    if userAnswer == questionAnswer:
        print("well done")
    else:
        print("incorrect")


def main(): 
    for question in range(0,2):
        rn1, rn2, answer = getQuestionNumbers()
        ua = getUserAnswer(rn1,rn2)
        printResult(ua,answer)

main()
