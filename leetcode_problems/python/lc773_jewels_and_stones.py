class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        map = dict()
        for char in stones:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

        count = 0
        for char in jewels:
            count += map.get(char, 0)

        return count


if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    print(Solution().numJewelsInStones(jewels, stones))
