playArea = [["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"]]

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

    for char in colAndrow:
        if char == ":":
            continue

        if IsColumnCharacter(char):
            column = char
            validAlpha = True
            
        if IsRowCharacter(char):
            row = char
            validNumeric = True

    

    if validAlpha and validNumeric:
        print("VALID CORDS!")
        listOfCords = ConvertColumnAndRowCordsToIndices(row, column)
        print(listOfCords)
        CheckIfSelectedCordHasBomb(playArea, listOfCords)

    else:
        print("INVALID CORDS!")

def IsColumnCharacter(character) -> bool:
    if character.isalpha():
        return True
    else:
        return False
    
def IsRowCharacter(character) -> bool:
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

    match row.upper():
        case "1":
            indices.append(0)
        case "2":
            indices.append(1)
        case "3":
            indices.append(2)
        case "4":
            indices.append(3)
        case "5":
            indices.append(4)
        case "6":
            indices.append(5)
        case "7":
            indices.append(6)
        case "8":
            indices.append(7)
    print(indices)
    return indices

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

while True:
    RenderPlayingField(playArea)
    userInput = input("Enter: ")
    SelectItemViaCord(userInput)
 
