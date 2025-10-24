class BombSpawningClass:

    def __init__(self) -> None:
        pass

    def SpawnBomb(self, playArea, rowAndColumn):
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