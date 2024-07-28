class Solution:
    def kItemsWithMaximumSum(
        self,
        numOnes: int,
        numZeros: int,
        numNegOnes: int,
        k: int,
    ) -> int:
        if k <= numOnes:
            return k

        k -= numOnes
        if k <= numZeros:
            return numOnes

        k -= numZeros
        return numOnes - k


if __name__ == "__main__":
    numOnes = 3
    numZeros = 2
    numNegOnes = 0
    k = 6

    print(Solution().kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))
