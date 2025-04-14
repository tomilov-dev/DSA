#include <vector>
using std::vector;

class Solution
{
public:
    int rob(vector<int> &nums)
    {
        int n = nums.size();
        if (n < 2)
        {
            return nums[0];
        }

        vector<int> dp(n + 1);
        dp[1] = nums[0];
        dp[2] = std::max(nums[1], dp[0]);
        for (int i = 2; i < n; i++)
        {
            dp[i + 1] = std::max(dp[i], dp[i - 1] + nums[i]);
        }
        return dp[n];
    }
};