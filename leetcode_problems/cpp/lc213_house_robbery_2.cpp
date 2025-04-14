#include <vector>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int dp(vector<int> &nums)
    {
        if (nums.size() == 1)
        {
            return nums[0];
        }

        int n = nums.size();
        vector<int> dp(n + 1);
        dp[1] = nums[0];
        dp[2] = std::max(nums[1], dp[1]);
        for (int i = 2; i < n; i++)
        {
            dp[i + 1] = std::max(dp[i], dp[i - 1] + nums[i]);
        }
        return dp[n];
    }

    int rob(vector<int> &nums)
    {
        if (nums.size() == 1)
        {
            return nums[0];
        }
        else if (nums.size() == 2)
        {
            return std::max(nums[0], nums[1]);
        }

        vector<int> nums1(nums.begin(), nums.end() - 1);
        vector<int> nums2(nums.begin() + 1, nums.end());
        return std::max(dp(nums1), dp(nums2));
    }
};