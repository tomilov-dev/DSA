class Solution:
    def sortPeople(
        self,
        names: list[str],
        heights: list[int],
    ) -> list[str]:
        return [
            r[0]
            for r in sorted(
                [(names[i], heights[i]) for i in range(len(names))],
                key=lambda x: x[1],
                reverse=True,
            )
        ]


if __name__ == "__main__":
    names = ["Mary", "John", "Emma"]
    heights = [180, 165, 170]

    print(Solution().sortPeople(names, heights))
