class Solution:
    def minOperations(self, logs: list[str]) -> int:
        steps = 0
        for log in logs:
            if log == "../":
                if steps > 0:
                    steps -= 1
            elif log == "./":
                pass
            else:
                steps += 1

        return steps


if __name__ == "__main__":
    logs = ["d1/", "d2/", "../", "d21/", "./"]
    print(Solution().minOperations(logs))
