class Validation:

    def IsColumnCharacterValid(character) -> bool:
        if character.isalpha():
            return True
        else:
            return False
        
    def IsValidCordValid(cord, cordAsList, colSize, rowSize) -> bool:
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
