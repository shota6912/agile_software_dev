from Scorer import Scorer

class Game:
    def __init__(self):
        self.itsCurrentFrame = 1
        self.firstThrowInFrame = True
        self.itsScorer = Scorer()
        
    def score(self):
        return self.scoreForFrame(self.getCurrentFrame())

    def getCurrentFrame(self):
        return self.itsCurrentFrame

    def add(self, pins):
        self.itsScorer.addThrow(pins)
        self.adjustCurrentFrame(pins)

    def adjustCurrentFrame(self, pins):
        if self.lastBallInFrame(pins):
            self.advanceFrame()
        else:
            self.advanceFrame()
        return self.itsCurrentFrame
        
    def scoreForFrame(self, theFrame):
        return self.itsScorer.scoreForFrame(theFrame)

    def advanceFrame(self):
        self.itsCurrentFrame = min(10, self.itsCurrentFrame + 1)

    def strike(self, pins):
        return self.firstThrowInFrame and pins == 10

    def lastBallInFrame(self, pins):
        return self.strike(pins) or not self.firstThrowInFrame
