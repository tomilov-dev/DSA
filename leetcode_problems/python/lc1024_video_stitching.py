class Solution:
    def videoStitching(
        self,
        clips: list[list[int]],
        time: int,
    ) -> int:
        clips.sort()
        p1 = -1
        p2 = 0
        count = 0

        for i, j in clips:
            if p2 >= time or i > p2:
                break
            elif p1 < i <= p2:
                count += 1
                p1 = p2
            p2 = max(p2, j)

        return count if p2 >= time else -1


if __name__ == "__main__":
    clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
    time = 10
    print(Solution().videoStitching(clips, time))
