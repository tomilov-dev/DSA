import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        h = []
        if a > 0:
            heapq.heappush(h, (-a, "a"))
        if b > 0:
            heapq.heappush(h, (-b, "b"))
        if c > 0:
            heapq.heappush(h, (-c, "c"))

        stk = []
        while h:
            x, char = heapq.heappop(h)
            if len(stk) >= 2 and stk[-2] == stk[-1] == char:
                if not h:
                    break
                y, nxt_char = heapq.heappop(h)
                stk.append(nxt_char)
                heapq.heappush(h, (x, char))
                if y + 1 < 0:
                    heapq.heappush(h, (y + 1, nxt_char))
            else:
                stk.append(char)
                if x + 1 < 0:
                    heapq.heappush(h, (x + 1, char))
        return "".join(stk)


class SolutionGreedy:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        def select() -> str | None:
            nonlocal a
            nonlocal b
            nonlocal c

            ca = a
            cb = b
            cc = c
            if len(stk) >= 2 and stk[-2] == stk[-1]:
                if stk[-1] == "a":
                    ca = 0
                elif stk[-1] == "b":
                    cb = 0
                elif stk[-1] == "c":
                    cc = 0

            char = None
            if ca > 0 and ca >= cb and ca >= cc:
                char = "a"
                a -= 1
            elif cb > 0 and cb >= ca and cb >= cc:
                char = "b"
                b -= 1
            elif cc > 0 and cc >= ca and cc >= cb:
                char = "c"
                c -= 1
            return char

        stk = []
        while a > 0 or b > 0 or c > 0:
            char = select()
            if char is None:
                break
            stk.append(char)
        return "".join(stk)


if __name__ == "__main__":
    print(SolutionGreedy().longestDiverseString(1, 1, 7))
