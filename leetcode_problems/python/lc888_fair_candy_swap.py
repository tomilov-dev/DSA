class Solution:
    def fairCandySwap(
        self,
        aliceSizes: list[int],
        bobSizes: list[int],
    ) -> list[int]:
        acount = sum(aliceSizes)
        bcount = sum(bobSizes)
        spread = (acount - bcount) // 2

        bset = set(bobSizes)
        for num in aliceSizes:
            k = num - spread
            if k in bset:
                return [num, k]

        return []


if __name__ == "__main__":
    aliceSizes = [2]
    bobSizes = [1, 3]
    print(Solution().fairCandySwap(aliceSizes, bobSizes))
