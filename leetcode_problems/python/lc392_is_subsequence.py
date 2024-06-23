"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) 
of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
"""


class Solution1(object):
    def run(self, string1: str, string2: str) -> bool:
        if not string1:
            return True

        pointer = 0
        for char in string2:
            if string1[pointer] == char:
                pointer += 1

            if pointer == len(string1):
                return True

        return False


if __name__ == "__main__":
    string1 = "abc"
    string2 = "ahbgdc"

    sol1 = Solution1()

    print(sol1.run(string1, string2))
