# Packages
import enum
import os

# Enums
class GameStates(enum.Enum): # Gamestates
    WIN = 1
    LOST = 2
    NEUTRAL = 3
class PlayerInputMenu(enum.Enum): # Options for the player.
    START = 1
    QUIT = 2


# Variables    
result = GameStates.NEUTRAL

# Function
def Play():

    # Clears screen 
    os.system('cls||clear')

    # Imports custom Classes
    
    from UserGameOptions import UserGameOptionsClass
    from SelectItemViaCord import SelectItemViaCordClass
    from PlayingField import PlayingFieldClass
    from GameEndLogic import GameEndLogicClass

    # Objects from Classes
    userGameOptionsObj = UserGameOptionsClass()
    selectItemViaCordObj = SelectItemViaCordClass()
    playingFieldObj = PlayingFieldClass()
    GameEndLogicObj = GameEndLogicClass("0", "X")

    # Starts the game via the Player's input
    playerInputMenuResult = userGameOptionsObj.GameStart(PlayerInputMenu)
    if playerInputMenuResult == PlayerInputMenu.START:
        while True:
            playingFieldObj.RenderPlayingField()
            userInput = input("Enter: ")
            
            if userGameOptionsObj.UserWantsToQuit(userInput):
                exit()
            else:   
                selectItemViaCordObj.SelectItemViaCord(userInput, playingFieldObj.colSize, playingFieldObj.rowSize, playingFieldObj.playArea)
                result = GameEndLogicObj.GameWinOrLose(playingFieldObj.playArea, GameStates)

                if result == GameStates.WIN or result == GameStates.LOST:
                    playingFieldObj.RenderPlayingField()
                    break

    elif playerInputMenuResult == PlayerInputMenu.QUIT:
        exit()

    # Prints out the result of the game.

def PrintResult():
       match result:
        case GameStates.WIN:
            print("You've won the game!")
        case GameStates.LOST:
            print("You've lost the game....")


# Runs the two main functions 
Play()
PrintResult()


# Issues
# Screen not clearning properly
