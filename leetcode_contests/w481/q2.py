class Solution:
    def minCost(self, s: str, cost: list[int]) -> int:
        charFreq = dict()
        charCost = dict()
        maxcost = 0
        for i, c in enumerate(s):
            charFreq[c] = charFreq.get(c, 0) + 1
            charCost[c] = charCost.get(c, 0) + cost[i]
            maxcost = max(maxcost, charCost[c])
        if len(charFreq) == 0:
            return 0
        total = 0
        maxcostfound = False
        for _, cost in charCost.items():
            if cost != maxcost or maxcostfound:
                total += cost
            elif cost == maxcost and not maxcostfound:
                maxcostfound = True
        return total


if __name__ == "__main__":
    s = "aabaac"
    cost = [1, 2, 3, 4, 1, 10]
    s = "abc"
    cost = [10, 5, 8]
    s = "zzzzz"
    cost = [67, 67, 67, 67, 67]
    print(Solution().minCost(s, cost))
