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

    def generatePrimes(self, max_value):
        if max_value >= 2:
            s = max_value + 1
            f = [True for i in range(s)]
            f[0] = f[1] = False

            for i in range(2, int(math.sqrt(s)) + 1):
                if f[i]:
                    for j in range(2 * i, s, i):
                        f[j] = False

            count = 0
            for i in range(s):
                if f[i]:
                    count += 1

            primes = [0 for i in range(count)]

            j = 0
            for i in range(s):
                if f[i]:
                    primes[j] = i
                    j += 1
            return primes

        else:
            return []
        
