class Solution:
    def bs(
        self,
        arr: list[str],
        target: str,
    ) -> int:
        lo = 0
        hi = len(arr) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            if arr[mid] > target:
                hi = mid
            else:
                lo = mid + 1

        return lo

    def nextGreatestLetter(
        self,
        letters: list[str],
        target: str,
    ) -> str:
        ind = self.bs(letters, target)
        if letters[ind] > target:
            return letters[ind]
        return letters[0]


if __name__ == "__main__":
    letters = ["c", "f", "j"]
    target = "z"
    print(Solution().nextGreatestLetter(letters, target))
