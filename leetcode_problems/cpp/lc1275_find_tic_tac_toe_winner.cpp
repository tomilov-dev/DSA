#include <string>
#include <vector>
#include <iostream>
using std::string;
using std::vector;

class Solution
{
public:
    string tictactoe(vector<vector<int>> &moves)
    {
        vector<vector<int>> board(3, vector<int>(3, -1));
        for (int i = 0; i < moves.size(); i++)
        {
            int pl = i % 2;
            board[moves[i][0]][moves[i][1]] = pl;
        }

        vector<vector<vector<int>>> combos = {
            {{0, 0}, {0, 1}, {0, 2}},
            {{1, 0}, {1, 1}, {1, 2}},
            {{2, 0}, {2, 1}, {2, 2}},
            {{0, 0}, {1, 0}, {2, 0}},
            {{0, 1}, {1, 1}, {2, 1}},
            {{0, 2}, {1, 2}, {2, 2}},
            {{0, 0}, {1, 1}, {2, 2}},
            {{2, 0}, {1, 1}, {0, 2}},
        };
        for (int combo_index = 0; combo_index < combos.size(); combo_index++)
        {
            vector<vector<int>> combo = combos[combo_index];
            bool is_win = true;
            int prev = board[combo[0][0]][combo[0][1]];
            if (prev == -1)
            {
                continue;
            }

            for (int i = 1; i <= 2; i++)
            {
                int i1 = combo[i][0];
                int i2 = combo[i][1];
                int cur = board[i1][i2];
                if (prev != cur)
                {
                    is_win = false;
                    break;
                }
            }
            if (is_win)
            {
                return (prev == 0) ? "A" : "B";
            }
        }

        if (moves.size() == 9)
        {
            return "Draw";
        }
        else
        {
            return "Pending";
        }
    }
};

class Solution2
{
public:
    string tictactoe(vector<vector<int>> &moves)
    {
        vector<int> rows(3, 0), cols(3, 0);
        int diag1 = 0, diag2 = 0;
        int player = 1;

        for (const auto &move : moves)
        {
            int row = move[0], col = move[1];
            rows[row] += player;
            cols[col] += player;
            if (row == col)
                diag1 += player;
            if (row + col == 2)
                diag2 += player;

            if (abs(rows[row]) == 3 || abs(cols[col]) == 3 || abs(diag1) == 3 || abs(diag2) == 3)
                return player == 1 ? "A" : "B";

            player = -player;
        }

        return moves.size() == 9 ? "Draw" : "Pending";
    }
};

int main()
{
    // vector<vector<int>> moves = {{0, 0}, {2, 0}, {1, 1}, {2, 1}, {2, 2}};
    vector<vector<int>> moves = {{0, 0}, {1, 1}, {2, 0}, {1, 0}, {1, 2}, {2, 1}, {0, 1}, {0, 2}, {2, 2}};
    Solution sol;
    auto res = sol.tictactoe(moves);
    std::cout << res << std::endl;
    return 0;
}