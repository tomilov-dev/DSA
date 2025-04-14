class SolutionWrong:
    def ambiguousCoordinates(self, s: str) -> list[str]:
        def backtrack(i: int, spaced: bool = False) -> None:
            if i >= n - 1:
                if not spaced:
                    return None

                res.append("".join(stack) + ")")
                return None

            stack.append(s[i])
            steps = [("", False)]
            if i < n - 2:
                steps += [(".", False), (", ", True)]

            for symb, space in steps:
                if space and spaced:
                    continue
                if stack[-1] == "0" and symb == "":
                    continue
                if len(stack) > 1 and stack[-2] == "." and symb == ".":
                    continue

                stack.append(symb)
                backtrack(i + 1, space or spaced)
                stack.pop()
            stack.pop()

        n = len(s)
        res = []
        stack = ["("]
        backtrack(1)
        return res


if __name__ == "__main__":
    s = "(123)"
    s = "(0123)"
    s = "(00011)"

    print(SolutionWrong().ambiguousCoordinates(s))
