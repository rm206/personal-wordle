from random_word import RandomWords
import enchant

ALLOWED_MAX_GUESSES = 6
dictionaryToCheck = enchant.Dict("en_US")

def wordForTheGame() -> str:
    r = RandomWords()
    word = r.get_random_word(hasDictionaryDef = "true", minDictionaryCount = 5, maxDictionaryCount = 10, minLength = 5, maxLength = 5)
    return word

def getGuess() -> str:
    guess = input("Enter guess : ")
    while (len(guess) != 5 or not dictionaryToCheck.check(guess)):
        if(len(guess) != 5):
            print("Enter 5 letter word only")
        else:
            print("Enter a meaningful word")
        guess = input("Enter guess : ")
    return guess

def checkAgainstAnswer(currentGuess : str, wordToGuess : str) -> list:
    indexWiseCheck = []
    for i in range(0, 5):
        if(currentGuess[i] == wordToGuess[i]):
            indexWiseCheck.append(True)
        else:
            indexWiseCheck.append(False)
    return indexWiseCheck

def checkIfWordGuessed(currentIndexCheckList : list) -> bool:
    if(False not in currentIndexCheckList):
        return True
    else:
        return False

def gameOverMessage(wordGuessed : str, wordToGuess : str):
    if wordGuessed:
        print("Game over. You guessed the word")
    else:
        print("You lose. The word was", wordToGuess)

def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def showStatusOfGuess(guesssesUsed : int, currentIndexCheckList : list, currentGuess : str, wordToGuess : str):
    setOfAnswer = set(wordToGuess)
    listOfGuess = list(currentGuess)
    for index, letter in enumerate(currentGuess):
        if (currentIndexCheckList[index] == True):
            print('', colored(65, 252, 3, letter), end = '', sep = '')
        elif (letter in setOfAnswer):
            print('', colored(252, 144, 3, letter), end = '', sep = '')
        else:
            print(letter, ' ', end = '', sep = '')
    print()

def startGuessing(wordToGuess : str):
    guesssesUsed = 0
    wordGuessed = False
    currentIndexCheckList = []

    while(guesssesUsed < ALLOWED_MAX_GUESSES and not wordGuessed):
        currentGuess = getGuess()
        currentGuess = currentGuess.lower()
        guesssesUsed += 1
        currentIndexCheckList = checkAgainstAnswer(currentGuess, wordToGuess)
        wordGuessed = checkIfWordGuessed(currentIndexCheckList)
        showStatusOfGuess(guesssesUsed, currentIndexCheckList, currentGuess, wordToGuess)
    
    gameOverMessage(wordGuessed, wordToGuess)

def main():
    # Generate random word
    wordToGuess = wordForTheGame()
    # Start the game
    startGuessing(wordToGuess)

if __name__ == "__main__":
    main()