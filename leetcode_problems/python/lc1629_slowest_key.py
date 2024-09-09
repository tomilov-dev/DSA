class Solution:
    def slowestKey(
        self,
        releaseTimes: list[int],
        keysPressed: str,
    ) -> str:
        for index in range(len(releaseTimes) - 1, 0, -1):
            releaseTimes[index] -= releaseTimes[index - 1]

        maxtime = max(releaseTimes)
        keys = [
            keysPressed[i]
            for i in range(len(keysPressed))
            if releaseTimes[i] == maxtime
        ]
        keys = sorted(list(set(keys)))
        return keys[-1]


if __name__ == "__main__":
    releaseTimes = [9, 29, 49, 50]
    keysPressed = "cbcd"
    print(Solution().slowestKey(releaseTimes, keysPressed))
