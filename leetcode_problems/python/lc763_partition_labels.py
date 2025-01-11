class Solution:
    def partitionLabels(
        self,
        s: str,
    ) -> list[int]:
        res = []
        mapper = dict()
        for i, c in enumerate(s):
            if c in mapper:
                mapper[c][1] = i
            else:
                mapper[c] = [i, None]

        i = 0
        while i < len(s):
            char = s[i]
            start, end = mapper.get(char)
            if end is None:
                res.append(1)
                i += 1
                continue

            maxi = 0
            local_end = end
            while True:
                while i <= local_end:
                    char = s[i]
                    _, cend = mapper.get(char)
                    cend = cend if cend else 0
                    maxi = max(maxi, cend)
                    i += 1

                if local_end == maxi:
                    break
                local_end = maxi

            res.append(maxi - start + 1)

        return res


class Solution2:
    def partitionLabels(
        self,
        s: str,
    ) -> list[int]:
        last_index = {c: i for i, c in enumerate(s)}

        res = []
        start, end = 0, 0

        for i, c in enumerate(s):
            end = max(end, last_index[c])
            if i == end:
                res.append(end - start + 1)
                start = i + 1

        return res


if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    print(Solution().partitionLabels(s))
