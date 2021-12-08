import os

class sub:
    def __init__(self,inpFile):
        self.calcF = inpFile
        self.outF = inpFile.split(".")[0] + ".log"

    