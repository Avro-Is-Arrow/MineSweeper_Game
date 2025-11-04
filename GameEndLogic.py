class GameEndLogicClass:
    import enum
    SafeIcon = ""
    BombIcon = ""

    def __init__(self, safeIcon, bombIcon) -> None:
        self.SafeIcon = safeIcon
        self.BombIcon = bombIcon
    

    def GameWinOrLose(self, playingArea) -> int:
        amountSafeIconAppears = 0

        for rows in playingArea:
            for icons in rows:
                if icons == self.SafeIcon:
                    amountSafeIconAppears += 1
                elif icons == self.BombIcon:
                    return 2
                else:
                    continue
            

                    
        if amountSafeIconAppears == 16:
            return 1
        else:
            return 3
        
