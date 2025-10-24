class UserGameOptions:
    import enum

    def GameStart(playerInputMenuEnums) -> enum.Enum:
        from InformationFile import InformationFile
        while(True):
            print("\n1: Start Game\n2: Quit Game\n3: Read Rules/Controls")
            userInput = input("Select Option: ")

            match userInput:
                case "1":
                    return playerInputMenuEnums.START
                case "2":
                    return playerInputMenuEnums.QUIT
                case "3":
                    InformationFile.Open()
                case _:
                    print("Invalid, try again. \n")
 
    def UserWantsToQuit(userInput) -> bool:
        if userInput.upper() == "QUIT":
            return True
        else:
            return False