import enum as Enum

class GameStates(Enum): # Gamestates
    WIN = 1
    LOST = 2
    
playArea = [["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"]]
colSize = 8
rowSize = 4

def RenderPlayingField(playArea : list):
    # Array, containing the play area.

    column = ["A", "B", "C", "D", "E", "F", "G", "H"]

    row = 1

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
                print(listOfCords)
                CheckIfSelectedCordHasBomb(playArea, listOfCords)
            else:
                    print("CORD ALREADY USED!")
        else:
            print(invalidCordMsg)
    else:
        print(invalidCordMsg)
   
def GameStart():
    ...
    
def GameWinOrLose(playingArea, gameStates) -> GameStates:
    ...

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
while True:
    
    RenderPlayingField(playArea)
    userInput = input("Enter: ")
    
    if UserWantsToQuit(userInput):
        exit()
    else:   
        SelectItemViaCord(userInput)
    
 
# Handle Index Out Of Range Errors FIXED
# Cords need to be switched in the other function, used the wrong indices... FIXED

# Game breaks once many grid areas are filled....
# Add GameOver AND Game Win (game wins once half of all 32 tiles are uncovered)
# Add Comments
# Fix grid rendering, everything is too close together.