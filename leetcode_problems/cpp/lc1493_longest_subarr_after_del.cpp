#include <vector>
#include <iostream>
#include <algorithm>

class Solution
{
public:
    int run(std::vector<int> &nums)
    {
        int max_count = 0;

        int zeros = 0;
        int walker = 0;
        int runner = 0;

        while (runner < nums.size())
        {
            zeros += (nums[runner] == 0);

            while (zeros > 1)
            {
                zeros -= (nums[walker] == 0);
                walker++;
            }

            max_count = std::max(max_count, runner - walker);
            runner++;
        }
        return max_count;
    }
};

int main()
{
    std::vector<int> nums = {1, 1, 0, 1};

    Solution sol;
    int answer = sol.run(nums);

    std::cout << answer << std::endl;
}