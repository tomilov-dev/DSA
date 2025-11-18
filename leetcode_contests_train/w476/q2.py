class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:
        stack = []
        for x in s:
            if not stack or stack[-1] == x:
                stack.append(x)
                continue
            else:
                stack.pop()
        return len(stack)
