class Solution:
    def vowelStrings(
        self,
        words: list[str],
        left: int,
        right: int,
    ) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        count = 0
        for i in range(min(left, len(words)), min(right + 1, len(words))):
            if words[i][0] in vowels and words[i][-1] in vowels:
                count += 1
        return count
