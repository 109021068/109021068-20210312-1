class Chess:
    def __init__(self, word, colour, move, size, number):
        self.studWord = word
        self.studColour = colour
        self.studMove =  move
        self.studSize = size
        self.studNumber = number
    def showInfo(self):
        print(self.studWord)
        print(self.studColour)
        print(self.studMove)
        print(self.studSize)
        print(self.studNumber)
x = Chess("將","black","straight line","maximum","1")
x1 = Chess("兵","red","point","smallest","5")
x2 = Chess("帥","red","straight line","maximum","1")
x.showInfo()
x1.showInfo()
x2.showInfo()
