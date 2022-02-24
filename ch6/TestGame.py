import unittest
from Game import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    # def testOneThrow(self):
    #     self.g.add(5)
    #     assert self.g.score() == 5
    #     assert self.g.getCurrentFrame() == 1

    def testTwoThrowNoMark(self):
        self.g.add(5)
        self.g.add(4)
        assert self.g.score() == 9

    def testFourThrowNoMark(self):
        self.g.add(5)
        self.g.add(4)
        self.g.add(7)
        self.g.add(2)
        assert self.g.score() == 18
        assert self.g.scoreForFrame(1) == 9
        assert self.g.scoreForFrame(2) == 18

    def testSimpleSpare(self):
        self.g.add(3)
        self.g.add(7)
        self.g.add(3)
        assert self.g.scoreForFrame(1) == 13

    def testSimpleFrameAfterSpare(self):
        self.g.add(3)
        self.g.add(7)
        self.g.add(3)
        self.g.add(2)
        assert self.g.scoreForFrame(1) == 13
        assert self.g.scoreForFrame(2) == 18
        assert self.g.score() == 18

    def testSimpleStrike(self):
        self.g.add(10)
        self.g.add(3)
        self.g.add(6)
        assert self.g.scoreForFrame(1) == 19
        assert self.g.score() == 28

    def testPerfectGame(self):
        for i in range(12):
            self.g.add(10)
        assert self.g.score() == 300

    def testEndOfArray(self):
        for i in range(9):
            self.g.add(0)
            self.g.add(0)
        self.g.add(2)
        self.g.add(8)
        self.g.add(10)

    def testSampleGame(self):
        self.g.add(1)
        self.g.add(4)
        self.g.add(4)
        self.g.add(5)
        self.g.add(6)
        self.g.add(4)
        self.g.add(5)
        self.g.add(5)
        self.g.add(10)
        self.g.add(0)
        self.g.add(1)
        self.g.add(7)
        self.g.add(3)
        self.g.add(6)
        self.g.add(4)
        self.g.add(10)
        self.g.add(2)
        self.g.add(8)
        self.g.add(6)
        assert self.g.score() == 133

    def testHeartBreak(self):
        for i in range(11):
            self.g.add(10)
        self.g.add(9)
        assert self.g.score() == 299

    def testTenthFrameSpare(self):
        for i in range(9):
            self.g.add(10)
        self.g.add(9)
        self.g.add(1)
        self.g.add(1)
        assert self.g.score() == 270

if __name__ == '__main__':
    unittest.main()