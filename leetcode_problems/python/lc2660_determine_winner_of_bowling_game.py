class Solution:
    def isWinner(
        self,
        player1: list[int],
        player2: list[int],
    ) -> int:
        def score(player: list[int], i: int) -> int:
            x = 1
            if i >= 1 and player[i - 1] == 10:
                x = 2
            if i >= 2 and player[i - 2] == 10:
                x = 2
            return player[i] * x

        score1 = 0
        score2 = 0
        n = len(player1)
        for i in range(n):
            score1 += score(player1, i)
            score2 += score(player2, i)

        if score1 > score2:
            return 1
        elif score2 > score1:
            return 2
        else:
            return 0
