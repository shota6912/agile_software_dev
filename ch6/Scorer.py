class Scorer:
    def __init__(self):
        self.ball = 0
        self.itsThrows = [0 for i in range(21)]
        self.itsCurrentThrow = 0

    def addThrow(self, pins):
        self.itsThrows[self.itsCurrentThrow] = pins
        self.itsCurrentThrow += 1
        
    def scoreForFrame(self, theFrame):
        self.ball = 0
        score = 0
        for currentFrame in range(0, theFrame):
            if self.strike():
                score += 10 + self.nextTwoBallsForStrike()
                self.ball += 1
            elif self.spare():
                score += 10 + self.nextBallForSpare()
                self.ball += 2
            else:
                score += self.twoBallsInFrame()
                self.ball += 2
        return score
        
    def strike(self):
        return self.itsThrows[self.ball] == 10

    def spare(self):
        return self.itsThrows[self.ball] + self.itsThrows[self.ball + 1] == 10

    def nextTwoBallsForStrike(self):
        return self.itsThrows[self.ball + 1] + self.itsThrows[self.ball + 2]

    def nextBallForSpare(self):
        return self.itsThrows[self.ball + 2]

    def twoBallsInFrame(self):
        return self.itsThrows[self.ball] + self.itsThrows[self.ball + 1]