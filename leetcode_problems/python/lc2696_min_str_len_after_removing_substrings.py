class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if len(stack) == 0:
                stack.append(char)
                continue

            if char == "B":
                if stack[-1] == "A":
                    stack.pop()
                else:
                    stack.append(char)

            elif char == "D":
                if stack[-1] == "C":
                    stack.pop()
                else:
                    stack.append(char)

            else:
                stack.append(char)

            print(stack)

        return len(stack)


if __name__ == "__main__":
    s = "ABFCACDB"
    print(Solution().minLength(s))
