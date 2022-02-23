import unittest
from GeneratePrimes import GeneratePrimes

class testGeneratePrimes(unittest.TestCase):

    def testPrimes(self):
        nullArray = GeneratePrimes().generatePrimes(0)
        assert len(nullArray) == 0
        minArray = GeneratePrimes().generatePrimes(2)
        assert len(minArray) == 1
        threeArray = GeneratePrimes().generatePrimes(3)
        assert len(threeArray) == 2
        assert threeArray[0] == 2
        assert threeArray[1] == 3
        centArray = GeneratePrimes().generatePrimes(100)
        assert len(centArray) == 25
        assert centArray[24] == 97

    def testExhaustive(self):
        for i in range(2, 500):
            self.__verifyPrimeList(GeneratePrimes().generatePrimes(i))

    def __verifyPrimeList(self, prime_list):
        for i in range(len(prime_list)):
            self.__verifyPrime(prime_list[i])

    def __verifyPrime(self, n):
        for factor in range(2, n):
            assert (n % factor) != 0

if __name__ == "__main__":
    unittest.main()