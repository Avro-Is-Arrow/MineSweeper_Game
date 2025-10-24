class GameEndLogicClass:
    import enum
    def __init__(self, safeIcon, bombIcon) -> None:
        self.safeIcon = safeIcon
        self.bombIcon = bombIcon
    

    def GameWinOrLose(self, playingArea, gameStates) -> enum.Enum:
        amountSafeIconAppears = 0

        for rows in playingArea:
            for icons in rows:
                if icons == self.safeIcon:
                    amountSafeIconAppears += 1

                elif icons == self.bombIcon:
                    return gameStates.LOST
                else:
                    continue
            

                    
        if amountSafeIconAppears == 16:
            return gameStates.WIN
        else:
            return gameStates.NEUTRAL
        
