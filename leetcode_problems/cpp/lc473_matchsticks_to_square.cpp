#include <vector>
#include <algorithm>
using std::max;
using std::vector;

class Solution
{
public:
    bool backtrack(int i, int t, vector<int> &m, int square[4])
    {
        if (i >= m.size())
        {
            for (int side = 0; side < 4; side++)
            {
                if (square[side] != t)
                {
                    return false;
                }
            }
            return true;
        }
        for (int side = 0; side < 4; side++)
        {
            if (square[side] + m[i] <= t)
            {
                square[side] += m[i];
                if (backtrack(i + 1, t, m, square))
                {
                    return true;
                }
                square[side] -= m[i];
            }

            if (square[side] == 0)
            {
                break;
            }
        }
        return false;
    }

    bool makesquare(vector<int> &matchsticks)
    {
        int sum = 0;
        for (int m : matchsticks)
        {
            sum += m;
        }

        if (sum <= 0 || sum % 4 != 0)
        {
            return false;
        }

        int t = sum / 4;
        if (*std::max_element(matchsticks.begin(), matchsticks.end()) > t)
        {
            return false;
        }

        std::sort(matchsticks.rbegin(), matchsticks.rend());
        int square[4] = {0, 0, 0, 0};
        return backtrack(0, t, matchsticks, square);
    }
};