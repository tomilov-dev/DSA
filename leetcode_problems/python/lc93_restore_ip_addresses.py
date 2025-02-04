class Solution:
    def restoreIpAddresses(
        self,
        s: str,
    ) -> list[str]:
        def backtrack(i: int, d: int) -> None:
            if d == 4 and i == len(s):
                res.append("".join(stack[:-1]))
                return
            if d > 4 or i >= len(s):
                return

            for j in range(1, 4):
                if i + j > len(s):
                    break
                segment = s[i : i + j]
                if (segment[0] == "0" and len(segment) > 1) or int(segment) > 255:
                    continue
                stack.append(segment)
                stack.append(".")
                backtrack(i + j, d + 1)
                stack.pop()
                stack.pop()

        res = []
        stack = []
        backtrack(0, 0)
        return res


if __name__ == "__main__":
    s = "25525511135"
    ex = "255.255.111.35"
    print(Solution().restoreIpAddresses(s))
