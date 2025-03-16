#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    bool is_good(int value, int target)
    {
        return value < target;
    }

    int searchInsert(vector<int> &nums, int target)
    {
        int low = -1;
        int high = nums.size();
        while (high - low > 1)
        {
            int mid = low + (high - low) / 2;
            if (is_good(nums[mid], target))
            {
                low = mid;
            }
            else
            {
                high = mid;
            }
        }
        return high;
    }
};

int main()
{
    vector<int> nums = {1, 3, 5, 6};
    int target = 5;
    Solution sol;
    int res = sol.searchInsert(nums, target);
    std::cout << res << std::endl;
    return 0;
}