#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    int missingNumber(vector<int> &nums)
    {
        long target_sum = 0;
        long current_sum = 0;
        for (int i = 0; i < nums.size() + 1; i++)
        {
            target_sum += i;
        }
        for (int num : nums)
        {
            current_sum += num;
        }
        return target_sum - current_sum;
    }
};

int main()
{
    vector<int> nums = {3, 0, 1};
    Solution sol;
    int res = sol.missingNumber(nums);
    std::cout << res << std::endl;
    return 0;
}