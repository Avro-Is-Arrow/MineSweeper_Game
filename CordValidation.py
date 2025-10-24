class ValidationClass:

    def __init__(self) -> None:
        pass

    def IsColumnCharacterValid(self, character: str) -> bool:
        if character.isalpha():
            return True
        else:
            return False
        
    def IsCordValid(self, cord, cordAsList, colSize, rowSize) -> bool:
        # if 99 != cordAsList[0] or 99 != cordAsList[1]:   
        if ':' == cord[1]:
            if cordAsList[0] < colSize and cordAsList[1] < rowSize:
                return True
            else:
                return False
        else:
            return False
        # else:
        #     return False

    def IsRowCharacterValid(self, character) -> bool:
        if character.isnumeric():
            return True
        else:
            return False
        
    def CordWasNotUsed(self, playArea, cordAsList) -> bool:
        if playArea[cordAsList[1]][cordAsList[0]] == "#":
            return True
        else:
            return False
