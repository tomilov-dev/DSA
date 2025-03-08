#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    int smallestEqual(vector<int> &nums)
    {
        for (int i = 0; i < nums.size(); i++)
        {
            if (i % 10 == nums[i])
            {
                return i;
            }
        }
        return -1;
    }
};

int main()
{
    vector<int> nums = {0, 1, 2};
    Solution sol;
    std::cout << sol.smallestEqual(nums) << std::endl;
    return 0;
}