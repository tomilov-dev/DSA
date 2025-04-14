from itertools import permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack():
            nonlocal count
            for i in range(0, n):
                if arr[i] <= 0:
                    continue

                arr[i] -= 1
                count += 1
                backtrack()
                arr[i] += 1

        count = 0
        arr = [0] * 26
        for char in tiles:
            arr[ord(char) - ord("A")] += 1
        n = len(arr)

        backtrack()
        return count


class SolutionMemo:
    def numTilePossibilities(self, tiles: str) -> int:
        unique_combinations = set()

        for length in range(1, len(tiles) + 1):
            for perm in permutations(tiles, length):
                unique_combinations.add(perm)

        return len(unique_combinations)


if __name__ == "__main__":
    tiles = "AAB"
    print(SolutionMemo().numTilePossibilities(tiles))
