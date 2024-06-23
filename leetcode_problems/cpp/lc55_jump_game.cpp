#include <vector>
#include <iostream>
#include <algorithm>
using std::vector;

class Solution
{
public:
    bool run(vector<int> &nums)
    {
        int last = nums.size() - 1;
        int index = nums.size() - 2;

        while (index >= 0)
        {
            if (index + nums[index] >= last)
            {
                last = index;
            }
            index--;
        }

        return last <= 0;
    }
};

int main()
{

    vector<int> nums = {2, 3, 1, 1, 4};

    Solution sol;
    bool answer = sol.run(nums);

    std::cout << answer << std::endl;
}