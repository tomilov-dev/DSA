class SolutionRecursive:
    def bf(
        self,
        digits: str,
        res: list[str],
        stack: list[str],
        index: int = 0,
    ) -> None:
        if len(stack) >= len(digits) or index >= len(digits):
            res.append("".join(stack))
            return None

        values = self.mapping[digits[index]]
        for value in values:
            stack.append(value)
            self.bf(digits, res, stack, index=index + 1)
            stack.pop()

    def letterCombinations(
        self,
        digits: str,
    ) -> list[str]:
        if not digits:
            return []

        self.mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }
        res = []
        self.bf(digits, res, [])
        return res


class SolutionIterative:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        stack = [("", 0)]
        result = []

        while stack:
            combination, index = stack.pop()
            if index == len(digits):
                result.append(combination)
                continue

            for letter in mapping[digits[index]]:
                stack.append((combination + letter, index + 1))

        return result


class SolutionNotation:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        combos = 1
        for digit in digits:
            combos *= len(mapping[digit])

        res = [""] * combos
        period = combos
        for digit in digits:
            period = period // len(mapping[digit])
            all_periods = combos // period // len(mapping[digit])
            i = 0
            for _ in range(all_periods):
                for value in mapping[digit]:
                    for _ in range(period):
                        res[i] += value
                        i += 1

        return res


if __name__ == "__main__":
    digits = "234"
    print(SolutionRecursive().letterCombinations(digits))
    print(SolutionIterative().letterCombinations(digits))
    print(SolutionNotation().letterCombinations(digits))
