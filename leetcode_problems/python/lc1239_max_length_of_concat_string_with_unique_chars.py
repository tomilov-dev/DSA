class Solution:
    def maxLength(
        self,
        arr: list[str],
    ) -> int:
        def backtrack(i: int) -> None:
            nonlocal count

            if i >= len(arr):
                count = max(count, len(mem))
                return

            for j in range(i, len(arr)):
                jset = set_arr[j]
                if len(jset) != len(arr[j]) or mem.intersection(jset):
                    continue

                mem.update(jset)
                count = max(count, len(mem))
                backtrack(j + 1)
                mem.difference_update(jset)

        set_arr = [set(s) for s in arr]
        mem = set()
        count = 0
        backtrack(0)
        return count


if __name__ == "__main__":
    arr = ["un", "iq", "ue"]
    # arr = ["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"]
    print(Solution().maxLength(arr))
