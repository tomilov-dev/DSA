class SolutionRecursive:
    def len(self, s: str) -> int:
        if len(s) <= 0:
            return 0
        return 1 + self.len(s[1:])


class SolutionRecursiveTailed:
    def len(self, s: str, l: int = 0) -> int:
        if len(s) <= 0:
            return l
        return self.len(s[1:], l + 1)


class SolutionIterative:
    def len(self, s: str) -> int:
        return sum(1 for _ in range(len(s)))


if __name__ == "__main__":
    s = "abcd"
    print(SolutionRecursive().len(s))
    print(SolutionRecursiveTailed().len(s))
    print(SolutionIterative().len(s))
