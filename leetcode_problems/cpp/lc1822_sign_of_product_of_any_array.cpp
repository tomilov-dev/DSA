#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    int arraySign(vector<int> &nums)
    {
        int m = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            if (nums[i] == 0)
            {
                return 0;
            }
            else if (nums[i] < 0)
            {
                m++;
            }
        }
        if (m % 2 == 0)
        {
            return 1;
        }
        else
        {
            return -1;
        }
    }
};

int main()
{
    vector<int> nums = {-1, -2, -3, -4, 3, 2, 1};
    Solution sol;
    std::cout << sol.arraySign(nums) << std::endl;
    return 0;
}