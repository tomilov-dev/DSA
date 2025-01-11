class Solution:
    def run(self, s: str) -> bool:
        count = 0
        for char in s:
            if count < 0:
                return False

            if char == "(":
                count += 1
            else:
                count -= 1

        return count == 0


if __name__ == "__main__":
    s = "((())))"
    print(Solution().run(s))
