#include <vector>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int minimumDifference(vector<int> &nums, int k)
    {
        int n = nums.size();
        std::sort(nums.begin(), nums.end());
        int max = 10000001;
        for (int i = 0; i <= n - k; i++)
        {
            max = std::min(max, nums[i + k - 1] - nums[i]);
        }
        return max;
    }
};