#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    bool is_good(int value, int target)
    {
        return value <= target;
    }

    int search(vector<int> &nums, int target)
    {
        int low = 0;
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
        return nums[low] == target ? low : -1;
    }
};

int main()
{
    vector<int> nums = {-1, 0, 3, 5, 9, 12};
    int target = 9;
    Solution sol;
    int res = sol.search(nums, target);
    std::cout << res << std::endl;
    return 0;
}