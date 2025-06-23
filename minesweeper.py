import enum


class GameStates(enum.Enum): # Gamestates
    WIN = 1
    LOST = 2
    
playArea = [["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"]]
colSize = 8
rowSize = 4
safeIcon = "O"
bombIcon = "X"


def RenderPlayingField(playArea : list):
    # Array, containing the play area.

    column = ["A", "B", "C", "D", "E", "F", "G", "H"]

    row = 1

 
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
    column = ""
    row = ""
    validNumeric = False
    validAlpha = False
    invalidCordMsg = "INVALID CORDS!"
    cordAlreadyUsed = "CORD ALREADY USED!"
   
    for char in colAndrow:
            if char == ":":
                continue

            if IsColumnCharacterValid(char):
                column = char
                validAlpha = True
                
            if IsRowCharacterValid(char):
                row = char
                validNumeric = True
        
    listOfCords = ConvertColumnAndRowCordsToIndices(row, column)

   
    if validAlpha and validNumeric:

        if IsValidCordValid(colAndrow, listOfCords):
            if CordWasNotUsed(playArea, listOfCords):
                CheckIfSelectedCordHasBomb(playArea, listOfCords)
            else:
                    print(cordAlreadyUsed)
        else:
            print(invalidCordMsg)
    else:
        print(invalidCordMsg)
   


def GameStart():
    ...
    
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
    

def IsColumnCharacterValid(character) -> bool:
    if character.isalpha():
        return True
    else:
        return False
    
def IsValidCordValid(cord, cordAsList) -> bool:
    if 99 != cordAsList[0] or 99 != cordAsList[1]:   
        if ':' == cord[1]:
            if cordAsList[0] < colSize and cordAsList[1] < rowSize:
                return True
    else:
        return False

def IsRowCharacterValid(character) -> bool:
    if character.isnumeric():
        return True
    else:
        return False

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

def UserWantsToQuit(userInput) -> bool:
    if userInput.upper() == "QUIT":
        return True
    else:
        return False



result = None
gameEnd = 0

import os
os.system('cls||clear')

while True:

    RenderPlayingField(playArea)
    userInput = input("Enter: ")
    
    if UserWantsToQuit(userInput):
        exit()
    else:   
        SelectItemViaCord(userInput)
        result = GameWinOrLose(playArea, GameStates)

        if result == GameStates.WIN or result == GameStates.LOST:
            RenderPlayingField(playArea)
            break
        
match result:
    case GameStates.WIN:
        print("You've won the game!")
    case GameStates.LOST:
        print("You've lost the game....")

        
# Handle Index Out Of Range Errors FIXED
# Cords need to be switched in the other function, used the wrong indices FIXED
# Game breaks once many grid areas are filled FIXED
# Add GameOver AND Game Win (game wins once half of all 32 tiles are uncovered) ADDED
# Fix grid rendering, everything is too close together FIXED

# Add Comments
# Add GameStart, giving instructions to the player when playing.
