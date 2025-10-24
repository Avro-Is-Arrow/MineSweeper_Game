class PlayingFieldClass:
    
    playArea = [["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"], 
            ["#", "#", "#", "#", "#", "#", "#", "#"]]
    colSize = 8
    rowSize = 4

    def RenderPlayingField(self):

        # Local Variables
        column = ["A", "B", "C", "D", "E", "F", "G", "H"]
        row = 1

    
        # Renders the Grid
        print()
        print(end="  ")
        for col in column:
            print(col, end=" ")
        print()
        for x in self.playArea:
            print(row, end=" ")
            row += 1
            for y in x:
                print(y, end=" ")
            print()