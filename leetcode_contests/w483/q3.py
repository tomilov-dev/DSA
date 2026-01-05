class Solution:
    def minimumCost(
        self,
        s: str,
        t: str,
        flipCost: int,
        swapCost: int,
        crossCost: int,
    ) -> int:
        n = len(s)
        zo = 0
        oz = 0
        for i in range(n):
            if s[i] != t[i] and s[i] == "0":
                zo += 1
            elif s[i] != t[i] and s[i] == "1":
                oz += 1

        total = 0
        pureSwap = min(zo, oz)
        total += min(pureSwap * swapCost, pureSwap * 2 * flipCost)

        crossSwap = (max(zo, oz) - pureSwap) // 2
        total += min(crossSwap * (swapCost + crossCost), crossSwap * 2 * flipCost)

        flipSwap = (max(zo, oz) - pureSwap) % 2
        total += flipSwap * flipCost

        return total


if __name__ == "__main__":
    s = "01000"
    t = "10111"
    flipCost = 10
    swapCost = 2
    crossCost = 2

    s = "001"
    t = "110"
    flipCost = 2
    swapCost = 100
    crossCost = 100

    s = "1010"
    t = "1010"
    flipCost = 5
    swapCost = 5
    crossCost = 5
    print(Solution().minimumCost(s, t, flipCost, swapCost, crossCost))
