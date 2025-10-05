class Solution:
    def removeSubstring(self, s: str, k: int) -> str:
        stack: list[tuple[str, int, int]] = []
        for i, char in enumerate(s):
            add_op = int(char == "(")
            add_cl = int(char == ")")
            if not stack:
                stack.append([char, add_op, add_cl])
            else:
                prev, op, cl = stack[-1]
                if char == prev:
                    stack.append([char, op + add_op, cl + add_cl])
                else:
                    if char == "(":
                        stack.append([char, add_op, cl + add_cl])
                    else:
                        stack.append([char, op + add_op, add_cl])

                cur, cur_op, cur_cl = stack[-1]
                if cur_op >= k and cur_cl >= k:
                    deletes = k * 2
                    while deletes and stack:
                        stack.pop()
                        deletes -= 1
        return "".join(x[0] for x in stack)


if __name__ == "__main__":
    s = "(())())"
    k = 1
    s = "((()))()()()"
    k = 3
    s = ")("
    k = 1
    print(Solution().removeSubstring(s, k))
