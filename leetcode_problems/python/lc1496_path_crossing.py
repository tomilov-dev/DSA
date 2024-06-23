"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.
Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. \
Return false otherwise.

Input: path = "NES"
Output: false 
Explanation: Notice that the path doesn't cross any point more than once.
"""


class Solution1(object):
    def run(self, path: str) -> bool:
        move = {
            "N": lambda pos: (pos[0], pos[1] + 1),
            "S": lambda pos: (pos[0], pos[1] - 1),
            "E": lambda pos: (pos[0] + 1, pos[1]),
            "W": lambda pos: (pos[0] - 1, pos[1]),
        }

        moves = set()
        pos = (0, 0)
        moves.add(pos)

        for direct in path:
            direct: str

            pos = move[direct](pos)
            if pos in moves:
                return True
            moves.add(pos)

        return False


if __name__ == "__main__":
    path = "SS"

    sol1 = Solution1()

    print(sol1.run(path))
