# Packages
import enum
import os


# Variables
playArea = [["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"]]
colSize = 8
rowSize = 4
safeIcon = "O"
bombIcon = "X"

# Enums
class GameStates(enum.Enum): # Gamestates
    WIN = 1
    LOST = 2
class PlayerInputMenu(enum.Enum): # Options for the player.
    START = 1
    QUIT = 2


# Functions
def RenderPlayingField(playArea : list):

    # Local Variables
    column = ["A", "B", "C", "D", "E", "F", "G", "H"]
    row = 1

 
    # Renders the Grid
    print()
    print(end="  ")
    for col in column:
        print(col, end=" ")
    print()
    for x in playArea:
        print(row, end=" ")
        row += 1
        for y in x:
            print(y, end=" ")
        print()
    
def SelectItemViaCord(colAndrow):
    from Validation import Validation

    # Local Variables
    column = ""
    row = ""
    validNumeric = False
    validAlpha = False
    invalidCordMsg = "INVALID CORDS!"
    cordAlreadyUsed = "CORD ALREADY USED!"
   
   # Checks to see if the user's input is in valid order.
    for char in colAndrow:
            if char == ":":
                continue

            if Validation.IsColumnCharacterValid(char):
                column = char
                validAlpha = True
                
            if Validation.IsRowCharacterValid(char):
                row = char
                validNumeric = True

    # Puts the cords that were inputted as a list, so it can be used.   
    listOfCords = ConvertColumnAndRowCordsToIndices(row, column)

   # Uses Cords
    if validAlpha and validNumeric:

        if Validation.IsValidCordValid(colAndrow, listOfCords, colSize, rowSize):
            if CordWasNotUsed(playArea, listOfCords):
                CheckIfSelectedCordHasBomb(playArea, listOfCords)
            else:
                    print(cordAlreadyUsed)
        else:
            print(invalidCordMsg)
    else:
        print(invalidCordMsg)
   
def GameWinOrLose(playingArea, gameStates) -> enum.Enum:
    amountSafeIconAppears = 0

    for rows in playingArea:
        for icons in rows:
            if icons == safeIcon:
                amountSafeIconAppears += 1

            elif icons == bombIcon:
                return gameStates.LOST
        

                
    if amountSafeIconAppears == 16:
        return gameStates.WIN
    
def ConvertColumnAndRowCordsToIndices(row, col) -> list:
    indices = []

    match col.upper():
        case "A":
            indices.append(0)
        case "B":
            indices.append(1)
        case "C":
            indices.append(2)
        case "D":
            indices.append(3)
        case "E":
            indices.append(4)
        case "F":
            indices.append(5)
        case "G":
            indices.append(6)
        case "H":
            indices.append(7)
        case _:
            indices.append(99)

            

    match row.upper():
        case "1":
            indices.append(0)
        case "2":
            indices.append(1)
        case "3":
            indices.append(2)
        case "4":
            indices.append(3)
        case _:
            indices.append(99)

    return indices

def CordWasNotUsed(playArea, cordAsList) -> bool:
    if playArea[cordAsList[1]][cordAsList[0]] == "#":
        return True
    else:
        return False

def CheckIfSelectedCordHasBomb(playArea, rowAndColumn) -> bool:
    import random as ran
    randomNum = ran.randrange(1, 10)
    column = rowAndColumn[0]
    row = rowAndColumn[1]

    if randomNum == 5:
        print("BOMB!")
        playArea[row][column] = "X"
    else:
        print("SAFE!")
        playArea[row][column] = "O"


# Game Logic, Gameplay

# Clears the play area on runtime.
os.system('cls||clear')

# Starts the game via the Player's input
from UserGameOptions import UserGameOptions
playerInputMenuResult = UserGameOptions.GameStart(PlayerInputMenu)
if playerInputMenuResult == PlayerInputMenu.START:
    while True:
        RenderPlayingField(playArea)
        userInput = input("Enter: ")
        
        if UserGameOptions.UserWantsToQuit(userInput):
            exit()
        else:   
            SelectItemViaCord(userInput)
            result = GameWinOrLose(playArea, GameStates)

            if result == GameStates.WIN or result == GameStates.LOST:
                RenderPlayingField(playArea)
                break
elif playerInputMenuResult == PlayerInputMenu.QUIT:
    exit()

# Prints out the result of the game.
match result:
    case GameStates.WIN:
        print("You've won the game!")
    case GameStates.LOST:
        print("You've lost the game....")


# Add Comments

