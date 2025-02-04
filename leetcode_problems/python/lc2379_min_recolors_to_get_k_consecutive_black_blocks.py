class Solution:
    def minimumRecolors(
        self,
        blocks: str,
        k: int,
    ) -> int:
        c = 0
        for b in blocks[:k]:
            c += int(b == "W")
        mini = c

        p1 = 1
        p2 = k
        while p1 < len(blocks) and p2 < len(blocks):
            c -= int(blocks[p1 - 1] == "W")
            c += int(blocks[p2] == "W")
            mini = min(mini, c)

            p1 += 1
            p2 += 1

        return mini


if __name__ == "__main__":
    blocks = "WBBWWBBWBW"
    k = 7
    print(Solution().minimumRecolors(blocks, k))
