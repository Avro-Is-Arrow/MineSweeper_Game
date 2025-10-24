class InformationFileClass:

    def __init__(self, textFileName):
        self.textFileName = textFileName

    def Open(self):
        import os
        os.startfile(self.textFileName)