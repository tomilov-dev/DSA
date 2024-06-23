"""
Given an array of characters chars, compress it using the following algorithm:
Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.
You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
"""
from time_measure import repeater


class Solution1:
    """
    58 ms, 16.6 MB

    Mean time = 0.01311 ms
    Min time  = 0.01231 ms
    """

    @repeater()
    def run(self, chars: list[str]) -> int:
        walker, runner = 0, 0
        while runner < len(chars):
            chars[walker] = chars[runner]
            count = 1

            while runner + 1 < len(chars) and chars[runner] == chars[runner + 1]:
                runner += 1
                count += 1

            if count > 1:
                for c in str(count):
                    chars[walker + 1] = c
                    walker += 1

            runner += 1
            walker += 1

        return walker


if __name__ == "__main__":
    chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]

    sol1 = Solution1()

    print(sol1.run(chars))
    print(chars)
