class Solution:
    def run(self, s: str) -> str:
        chars = list(s)
        p1 = len(chars) - 1

        spaces = chars.count(" ")
        p2 = -1 + len(chars) + spaces * 2
        chars.extend([""] * spaces * 2)

        while p1 >= 0 and p2 >= 0:
            if chars[p1] == " ":
                crep = ["0", "4", "@"]
                for char in crep:
                    chars[p2] = char
                    p2 -= 1
            else:
                chars[p2] = chars[p1]
                p2 -= 1
            p1 -= 1

        return "".join(chars)


if __name__ == "__main__":
    s = "Hello World"
    print(Solution().run(s))
