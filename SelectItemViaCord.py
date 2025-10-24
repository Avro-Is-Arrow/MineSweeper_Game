class SelectItemViaCordClass:
    def __init__(self) -> None:
        pass
    
    # Private Method, for internal use only.
    def private_convertColumnAndRowCordsToIndices_(self, row, col) -> list:
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
                indices.append(99)  # Fall back

                

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
                indices.append(99) # Fall back

        return indices


    def SelectItemViaCord(self, colAndrow, colSize, rowSize, playArea):
        from CordValidation import ValidationClass
        from BombSpawn import BombSpawningClass

        # Object Instatiation
        validationObj = ValidationClass()
        bombSpawningObj = BombSpawningClass()


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

                if validationObj.IsColumnCharacterValid(char):
                    column = char
                    validAlpha = True
                    
                if validationObj.IsRowCharacterValid(char):
                    row = char
                    validNumeric = True

        # Puts the cords that were inputted as a list, so it can be used.   
        listOfCords = SelectItemViaCordClass.private_convertColumnAndRowCordsToIndices_(self, row, column)

    # Uses Cords
        if validAlpha and validNumeric:

            if validationObj.IsCordValid(colAndrow, listOfCords, colSize, rowSize):
                if validationObj.CordWasNotUsed(playArea, listOfCords):
                    bombSpawningObj.SpawnBomb(playArea, listOfCords)
                else:
                        print(cordAlreadyUsed)
            else:
                print(invalidCordMsg)
        else:
            print(invalidCordMsg)