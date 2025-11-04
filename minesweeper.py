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


# Function
def PrintResult(gameResult):
       match gameResult:
        case GameStates.WIN.value:
            print("You've won the game!")
        case GameStates.LOST.value:
            print("You've lost the game....")

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
            userInput = input("Enter1: ")
            
            if userGameOptionsObj.UserWantsToQuit(userInput):
                exit()
            else:   
                selectItemViaCordObj.SelectItemViaCord(userInput, playingFieldObj.colSize, playingFieldObj.rowSize, playingFieldObj.playArea)
                result = GameEndLogicObj.GameWinOrLose(playingFieldObj.playArea) # Returns 1 = WIN, 2 = LOST, 3 = NEUTRAL

                if result == GameStates.WIN.value or result == GameStates.LOST.value: # Casts the Enum into an int for condition
                    playingFieldObj.RenderPlayingField()
                    PrintResult(result)
                    break

    elif playerInputMenuResult == PlayerInputMenu.QUIT:
        exit()

    # Prints out the result of the game.




# Runs the two main functions 
Play()


# Issues
# Screen not clearning properly
# Order, safe should comes AFTER scene is rendered.
