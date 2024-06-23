#include <vector>
#include <iostream>

class Solution
{
public:
    int run(std::vector<int> &nums)
    {
        for (int index = 0; index < nums.size(); index++)
        {
            int left = 0;
            int right = 0;
            for (int i = 0; i < index; i++)
            {
                left += nums[i];
            }
            for (int j = index + 1; j < nums.size(); j++)
            {
                right += nums[j];
            }
            if (left == right)
            {
                return index;
            }
        }
        return -1;
    }

    int run2(std::vector<int> &nums)
    {
        int left = 0;
        int right = 0;

        for (auto num : nums)
        {
            right += num;
        }

        for (int index = 0; index < nums.size(); index++)
        {
            right -= nums[index];
            if (left == right)
            {
                return index;
            }
            left += nums[index];
        }

        return -1;
    }
};

int main()
{
    std::vector<int> nums = {1, 7, 3, 6, 5, 6};

    Solution sol;
    int answer = sol.run2(nums);

    std::cout << answer << std::endl;
    return 0;
}