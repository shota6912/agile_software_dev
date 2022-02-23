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
        
