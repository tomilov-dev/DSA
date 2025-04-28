#include <vector>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int n = nums.size();
        vector<int> dp(n, 0);
        dp[0] = nums[0];
        for (int i = 1; i < n; i++)
        {
            dp[i] = std::max(dp[i - 1] + nums[i], nums[i]);
        }
        int max = -100000;
        for (int num : dp)
        {
            max = std::max(max, num);
        }
        return max;
    }
};