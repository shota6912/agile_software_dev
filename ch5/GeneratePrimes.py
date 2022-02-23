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
    def __init__(self):
        pass

    def generatePrimes(self, maxValue):
        if maxValue < 2:
            return []

        else:
            self.initializeSieve(maxValue)
            self.sieve()
            self.loadPrimes()
            return self.primes

    def loadPrimes(self):
        self.count = 0
        for i in range(self.s):
            if self.f[i]:
                self.count += 1

        self.primes = [0 for i in range(self.count)]      
        j = 0
        for i in range(self.s):
            if self.f[i]:
                self.primes[j] = i
                j += 1
        return self.primes

    def sieve(self):
        for i in range(2, int(math.sqrt(self.s)) + 1):
            if self.f[i]:
                for j in range(2 * i, self.s, i):
                    self.f[j] = False

    def initializeSieve(self, maxValue):
        self.s = maxValue + 1
        self.f = [True for i in range(self.s)]
        self.f[0] = self.f[1] = False
