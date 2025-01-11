class Solution:
    def findThePrefixCommonArray(
        self,
        A: list[int],
        B: list[int],
    ) -> list[int]:
        s1 = set()
        s2 = set()
        res = []
        i = 0
        while i < len(A):
            s1.add(A[i])
            s2.add(B[i])
            res.append(len(s1.intersection(s2)))
            i += 1

        return res


class Solution:
    def findThePrefixCommonArray(
        self,
        A: list[int],
        B: list[int],
    ) -> list[int]:
        s1 = [False for _ in range(len(A) + 1)]
        s2 = [False for _ in range(len(B) + 1)]
        res = []

        for i in range(len(A)):
            s1[A[i]] = True
            s2[B[i]] = True

            common = 0
            for j in range(len(s1)):
                common += int(s1[j] and s2[j])
            res.append(common)

        return res


class Solution:
    def findThePrefixCommonArray(
        self,
        A: list[int],
        B: list[int],
    ) -> list[int]:
        s1 = 0
        s2 = 0
        res = []
        for i in range(len(A)):
            s1 = s1 | 1 << A[i]
            s2 = s2 | 1 << B[i]
            common = 0

            num = s1 & s2
            while num != 0:
                common += num % 2
                num //= 2
            res.append(common)

        return res
