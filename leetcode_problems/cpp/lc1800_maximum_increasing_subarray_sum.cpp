#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    int maxAscendingSum(vector<int> &nums)
    {
        int maxsum = nums[0];
        int cursum = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[i] > nums[i - 1])
            {
                cursum += nums[i];
            }
            else
            {
                maxsum = std::max(cursum, maxsum);
                cursum = nums[i];
            }
            if (i == nums.size() - 1)
            {
                maxsum = std::max(cursum, maxsum);
            }
        }
        return maxsum;
    }
};

int main()
{
    vector<int> nums = {10, 20, 30, 5, 10, 50};
    Solution sol;
    int res = sol.maxAscendingSum(nums);
    std::cout << res << std::endl;
    return 0;
}