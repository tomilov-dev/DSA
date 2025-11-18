class Solution:
    def recoverOrder(
        self,
        order: list[int],
        friends: list[int],
    ) -> list[int]:
        mp = dict()
        for i, v in enumerate(order):
            mp[v] = i

        res = []
        for f in friends:
            res.append((mp[f], f))

        res.sort(key=lambda x: x[0])
        return [x[1] for x in res]


if __name__ == "__main__":
    order = [3, 1, 2, 5, 4]
    friends = [1, 3, 4]
    sol = Solution()
    print(sol.recoverOrder(order, friends))
