#include <vector>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int findLHS(vector<int> &nums)
    {
        std::sort(nums.begin(), nums.end());
        int p1 = 0;
        int p2 = 0;
        int max = 0;
        while (p1 < nums.size() && p2 < nums.size())
        {
            if (nums[p2] - nums[p1] == 1)
            {
                max = std::max(max, p2 - p1 + 1);
                p2++;
            }
            else if (nums[p2] - nums[p1] > 1)
            {
                p1++;
            }
            else
            {
                p2++;
            }
        }
        return max;
    }
};