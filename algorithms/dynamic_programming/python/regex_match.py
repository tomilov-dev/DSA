from abc import ABC
from abc import abstractmethod
from pprint import pprint


class ISolution(ABC):
    @abstractmethod
    def match(self, t: str, p: str) -> bool:
        pass


class SolutionRecursive(ISolution):
    def match(self, t: str, p: str) -> bool:
        def isblank(p: str) -> bool:
            """
            Проверка, "нулевой" ли паттерн
            """
            if not p:
                return True
            for i in range(len(p)):
                if i % 2 == 1 and p[i] != "*":
                    return False
            return p[-1] == "*"

        def iseq(i: int, j: int) -> bool:
            if i >= tn or j >= pn:
                return False
            return t[i] == p[j] or p[j] == "."

        def rec(i: int, j: int) -> bool:
            if j == pn:
                # Кончился паттерн. Проверка конца строки.
                return i == tn
            if i == tn:
                # Кончилась строка. Проверка, "нулевой" ли паттерн.
                return isblank(p[j:])

            if j + 1 < pn and p[j + 1] == "*":
                skip = rec(i, j + 2)
                use = iseq(i, j) and rec(i + 1, j)
                return skip or use

            else:
                return iseq(i, j) and rec(i + 1, j + 1)

        tn = len(t)
        pn = len(p)
        return rec(0, 0)


class SolutionTopDown(ISolution):
    def match(self, t: str, p: str) -> bool:
        def isblank(p: str) -> bool:
            """
            Проверка, "нулевой" ли паттерн
            """
            if not p:
                return True
            if len(p) % 2 != 0:
                return False
            for i in range(1, len(p), 2):
                if p[i] != "*":
                    return False
            return True

        def iseq(i: int, j: int) -> bool:
            if i >= tn or j >= pn:
                return False
            return t[i] == p[j] or p[j] == "."

        def rec(i: int, j: int) -> bool:
            if j == pn:
                # Кончился паттерн. Проверка конца строки.
                return i == tn
            if i == tn:
                # Кончилась строка. Проверка, "нулевой" ли паттерн.
                return isblank(p[j:])

            key = (i, j)
            if key not in mem:
                if j + 1 < pn and p[j + 1] == "*":
                    skip = rec(i, j + 2)
                    use = iseq(i, j) and rec(i + 1, j)
                    mem[key] = skip or use

                else:
                    mem[key] = iseq(i, j) and rec(i + 1, j + 1)
            return mem[key]

        tn = len(t)
        pn = len(p)
        mem = {}
        return rec(0, 0)


class SolutionBottomUp(ISolution):
    def match(self, t: str, p: str) -> bool:
        tn = len(t)
        pn = len(p)
        dp = [[False] * (tn + 1) for _ in range(pn + 1)]
        dp[0][0] = True

        # Инициализация: паттерн против пустой строки
        for i in range(2, pn + 1):
            if p[i - 1] == "*" and dp[i - 2][0]:
                dp[i][0] = True

        for i in range(1, pn + 1):
            for j in range(1, tn + 1):
                if p[i - 1] == "*" and i >= 2:
                    # Пропустить символ + *
                    dp[i][j] = dp[i - 2][j]
                    # Или использовать * для текущего символа строки
                    if p[i - 2] == t[j - 1] or p[i - 2] == ".":
                        dp[i][j] = dp[i][j] or dp[i][j - 1]
                else:
                    if p[i - 1] == t[j - 1] or p[i - 1] == ".":
                        dp[i][j] = dp[i - 1][j - 1]

        return dp[pn][tn]


class SolutionBottomUpOptimized(ISolution):
    def match(self, t: str, p: str) -> bool:
        tn = len(t)
        pn = len(p)
        prev2 = [False] * (tn + 1)  # dp[i-2][*]
        prev = [False] * (tn + 1)  # dp[i-1][*]
        cur = [False] * (tn + 1)  # dp[i][*]
        prev[0] = True

        for i in range(1, pn + 1):
            cur[0] = False
            if p[i - 1] == "*" and i >= 2 and prev2[0]:
                cur[0] = True

            for j in range(1, tn + 1):
                if p[i - 1] == "*":
                    cur[j] = False
                    # Пропустить символ + *
                    if i >= 2 and prev2[j]:
                        cur[j] = True
                    # Использовать * для текущего символа строки
                    if (
                        i >= 2
                        and (p[i - 2] == t[j - 1] or p[i - 2] == ".")
                        and cur[j - 1]
                    ):
                        cur[j] = True
                else:
                    cur[j] = prev[j - 1] and (p[i - 1] == t[j - 1] or p[i - 1] == ".")
            prev2, prev, cur = prev, cur, [False] * (tn + 1)
        return prev[tn]


def test_regex_match(
    solution: ISolution,
    show_tests: bool = False,
) -> None:
    cases = [
        # (text, pattern, expected_result)
        ("", "", True),
        ("", "a*", True),
        ("", "a*b*", True),
        ("a", "a", True),
        ("a", ".", True),
        ("ab", "a.", True),
        ("ab", ".*", True),
        ("ab", "a*", False),
        ("aaa", "a*", True),
        ("ab", "a*ab", True),
        ("mississippi", "mis*is*p*.", False),
        ("ab", ".*c", False),
        ("aab", "c*a*b", True),
        ("aaa", "ab*a*c*a", True),
        ("abcd", "d*", False),
        ("", ".*", True),
        ("abc", "abc*", True),
        ("abc", "abc*.", True),
        ("abc", "a.c", True),
        ("abc", "a.*c", True),
    ]
    passed = 0
    print(f"\nTest {'-'*5} {solution.__class__.__name__} {'-'*5}")
    for idx, (t, p, expected) in enumerate(cases, 1):
        result = solution.match(t, p)
        if show_tests:
            print(f"Test {idx}: match({t!r}, {p!r}) == {expected} -> {result}")
        if result == expected:
            passed += 1
    print(f"Passed {passed} out of {len(cases)} tests.")


if __name__ == "__main__":
    test_regex_match(SolutionRecursive())
    test_regex_match(SolutionTopDown())
    test_regex_match(SolutionBottomUp())
    test_regex_match(SolutionBottomUpOptimized())
