class Solution:
    def minRemoveToMakeValid(
        self,
        s: str,
    ) -> str:
        stack = []
        to_del = []
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if not stack:
                    to_del.append(index)
                else:
                    stack.pop()
            else:
                continue

        to_del += stack
        to_del = set(to_del)
        new = []
        for index, char in enumerate(s):
            if index in to_del:
                continue
            new.append(char)
        return "".join(new)


class Solution:
    def minRemoveToMakeValid(
        self,
        s: str,
    ) -> str:
        new = list(s)
        stack = []
        for index, char in enumerate(new):
            if char == "(":
                stack.append(index)
            elif char == ")":
                if not stack:
                    new[index] = ""
                else:
                    stack.pop()

        for index in stack:
            new[index] = ""
        return "".join(new)


if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(Solution().minRemoveToMakeValid(s))
