#include <vector>
#include <iostream>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int run(vector<int> &nums)
    {
        int counter = 0;
        int last = nums.size() - 1;
        while (last > 0)
        {
            int index = 0;
            while (index < last)
            {
                if (index + nums[index] >= last)
                {
                    break;
                }
                index++;
            }
            last = index;
            counter++;
        }

        return counter;
    }

    int run2(vector<int> &nums)
    {
        int counter = 0;
        int p1 = 0;
        int p2 = 0;

        for (int i = 0; i < nums.size() - 1; i++)
        {
            p2 = std::max(p2, i + nums[i]);
            if (i == p1)
            {
                counter++;
                p1 = p2;
            }
        }
        return counter;
    }
};

int main()
{
    vector<int> nums = {2, 3, 1, 1, 4};
    // vector<int> nums = {2, 3, 0, 1, 4};
    // vector<int> nums = {1, 1, 1, 1};

    Solution sol;
    int answer = sol.run2(nums);

    std::cout << answer << std::endl;
}
