class Solution:
    def to_min(self, time: str) -> int:
        return int(time.split(":")[0]) * 60 + int(time.split(":")[-1])

    def convertTime(self, current: str, correct: str) -> int:
        cur_min = self.to_min(current)
        cor_min = self.to_min(correct)
        spread = cor_min - cur_min
        ti = 0
        times = [60, 15, 5, 1]
        ops = 0
        while spread:
            while ti < len(times) and times[ti] > spread:
                print(times[ti], spread)
                ti += 1

            spread -= times[ti]
            ops += 1

        return ops


if __name__ == "__main__":
    current = "02:30"
    correct = "04:35"
    print(Solution().convertTime(current, correct))
