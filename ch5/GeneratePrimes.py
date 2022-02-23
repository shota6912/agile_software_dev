"""
This class Generates prime numbers up to a suser specified maximum.
the algorithm used is the Sieve of Eratosthenes.

Erastosthenes of Cyrene, b. c. 276 BC, Cyrene, Libya
d. c. 194, Alexandria. The first man to calculate the circumference
of the Earth. Also known for working on calendars with leap
years and ran the library at Alexandria.

The algorithm is quite simple. Given an array of integers starting
at 2. Cross out all multiples of 2. Find the next uncrossed 
integer, and cross out all of its multiples. Repeat until
you have passed the aquare root of the maximum value.
"""

import math

class GeneratePrimes:

    def generatePrimes(self, maxValue):
        if maxValue < 2:
            return []

        else:
            self.uncrossIntegersUpTo(maxValue)
            self.crossOutMultiples()
            self.putUncrossedIntegersIntoResult()
            return self.result

    def uncrossIntegersUpTo(self, maxValue):
        self.crossedOut = [False for i in range(maxValue + 1)]
        self.crossedOut[0] = self.crossedOut[1] = True

    def crossOutMultiples(self):
        maxPrimeFactor = self.calcMaxPrimeFactor()
        for i in range(2, maxPrimeFactor):
            if self.notCrossed(i):
                self.crossOutMultipleOf(i)

    def calcMaxPrimeFactor(self):
        maxPrimeFactor = int(math.sqrt(len(self.crossedOut))) + 1
        return maxPrimeFactor

    def crossOutMultipleOf(self, i):
        for multiple in range(2 * i, len(self.crossedOut), i):
            self.crossedOut[multiple] = True

    def notCrossed(self, i):
        return self.crossedOut[i] == False

    def putUncrossedIntegersIntoResult(self):
        self.result = [0 for i in range(self.numberOfUncrossedIntegers())]      
        j = 0
        for i in range(len(self.crossedOut)):
            if self.notCrossed(i):
                self.result[j] = i
                j += 1

    def numberOfUncrossedIntegers(self):
        count = 0
        for i in range(len(self.crossedOut)):
            if self.notCrossed(i):
                count += 1
        return count
