"""
A string s is nice if, for every letter of the alphabet that s contains, 
it appears both in uppercase and lowercase. 
For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. 
However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. 
If there are multiple, return the substring of the earliest occurrence. 
If there are none, return an empty string.

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter 
of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
"""


def isNice(s: str) -> bool:
    mapper = dict()

    for letter in s:
        mapper[letter] = True

    for letter in mapper:
        letter: str
        if letter.islower():
            if letter.upper() not in mapper:
                return False
        else:
            if letter.lower() not in mapper:
                return False

    return True


def longestNiceSubstringBruteforce(s: str) -> str:
    start = 0

    substing = ""
    for ind1 in range(start, len(s)):
        for ind2 in range(len(s), start, -1):
            sub = s[ind1:ind2]
            if isNice(sub):
                if len(sub) > len(substing):
                    substing = sub
        start += 1

    if len(substing) >= 2:
        return substing
    return ""


def longestNiceSubstringRecursive(s: str) -> str:
    if not s:
        return ""

    charset = set(s)
    for index, char in enumerate(s):
        if char.swapcase() not in charset:
            s0 = longestNiceSubstringRecursive(s[:index])
            s1 = longestNiceSubstringRecursive(s[index + 1 :])
            return max(s0, s1, key=len)

    return s


if __name__ == "__main__":
    # s = "abABB"
    # s = "abA"
    # s = "YazaAay"
    s = "qQUjJ"

    # sub = longestNiceSubstringBruteforce(s)
    sub = longestNiceSubstringRecursive(s)
    print(sub)
