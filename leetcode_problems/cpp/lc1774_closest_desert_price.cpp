#include <vector>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int get_min(int total, int target, int min)
    {
        int sp1 = target - total;
        int sp2 = target - min;
        if (std::abs(sp1) > std::abs(sp2))
        {
            return min;
        }
        else if (std::abs(sp1) < std::abs(sp2))
        {
            return total;
        }
        else
        {
            return sp1 > sp2 ? total : min;
        }
    }

    void bactrack(int i, int &total, int &target, int &min, vector<int> &tc)
    {
        if (total >= target)
        {
            min = get_min(total, target, min);
            return;
        }
        if (i >= tc.size())
        {
            min = get_min(total, target, min);
            return;
        }

        bactrack(i + 1, total, target, min, tc);
        total += tc[i];
        bactrack(i + 1, total, target, min, tc);
        total += tc[i];
        bactrack(i + 1, total, target, min, tc);
        total -= 2 * tc[i];
    }

    int closestCost(vector<int> &baseCosts, vector<int> &toppingCosts, int target)
    {
        int min = 100000000;
        int total = 0;
        for (int bc : baseCosts)
        {
            total += bc;
            bactrack(0, total, target, min, toppingCosts);
            total -= bc;
        }
        return min;
    }
};