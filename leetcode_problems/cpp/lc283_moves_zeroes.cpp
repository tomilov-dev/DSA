#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    void run(vector<int> &nums)
    {
        int walker = 0;
        for (int runner = 0; runner < nums.size(); runner++)
        {
            if (nums[walker] != 0)
            {
                walker++;
            }
            else if (nums[runner] != 0)
            {
                nums[walker] = nums[runner];
                nums[runner] = 0;
                walker++;
            }
        }
    }
};

int main()
{
    vector<int> nums = {0, 1, 0, 3, 12};

    Solution sol;
    sol.run(nums);

    for (int num : nums)
    {
        std::cout << num << std::endl;
    }
}