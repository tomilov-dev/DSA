class Solution:
    def is_prime(self, n: int) -> bool:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        count = 0
        for i in range(2, n):
            count += self.is_prime(i)
        return count


class Solution:
    def countPrimes(self, n: int) -> int:
        primes = [True] * max(2, n)
        primes[0] = False
        primes[1] = False
        for i in range(2, (n // 2) + 1):  # range(2, (n ** 0.5)+ 1) or range(2, n)
            if not primes[i]:
                continue
            for j in range(i * i, n, i):
                primes[j] = False
        return sum(primes)
