import unittest
from Frame import Frame

class TestFrame(unittest.TestCase):
    def testScoreNoThrows(self):
        f = Frame()
        f.add(5)
        assert f.getScore() == 5

if __name__ == '__main__':
    unittest.main()