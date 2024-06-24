"""
Write a function that takes the binary representation of a positive integer 
and returns the number of 
set bits it has (also known as the Hamming weight).

Example 1:
Input: n = 11
Output: 3
Explanation: The input binary string 1011 has a total of three set bits.
"""


def hammingWeightGreedy(n: int) -> int:
    cur_n = n
    count = 0

    while cur_n > 0:
        degree = 0

        while (2**degree) <= cur_n:
            degree += 1

        cur_n -= 2 ** (max(degree - 1, 0))
        count += 1

    return count


def hammingWeightRecursive(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return hammingWeightRecursive(n & (n - 1)) + 1


if __name__ == "__main__":
    n = 128
    hw = hammingWeightGreedy(n)
    print(hw)
