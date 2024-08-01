class Solution:
    def sortTheStudents(
        self,
        score: list[list[int]],
        k: int,
    ) -> list[list[int]]:
        return sorted(score, key=lambda x: x[k], reverse=True)


if __name__ == "__main__":
    score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
    k = 2

    print(Solution().sortTheStudents(score, k))
