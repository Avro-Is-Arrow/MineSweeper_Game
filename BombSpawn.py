class BombSpawningClass:
    SafeIcon = ""
    BombIcon = ""

    def __init__(self, safeIcon, bombIcon) -> None:
        self.SafeIcon = safeIcon
        self.BombIcon = bombIcon

    def SpawnBomb(self, playArea, rowAndColumn):
        import random as ran
        randomNum = ran.randrange(1, 10)
        column = rowAndColumn[0]
        row = rowAndColumn[1]

        if randomNum == 5:
            print("BOMB!")
            playArea[row][column] = self.BombIcon
        else:
            print("SAFE!")
            playArea[row][column] = self.SafeIcon