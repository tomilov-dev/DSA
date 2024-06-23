#include <vector>
#include <iostream>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int run(vector<int> &nums, int k)
    {
        int walker = 0;
        int runner = 0;

        while (runner < nums.size())
        {
            if (nums[runner] == 0)
            {
                k--;
            }
            if (k < 0)
            {
                if (nums[walker] == 0)
                {
                    k++;
                }
                walker++;
            }
            runner++;
        }

        return runner - walker;
    }
};

int main()
{
    vector<int> nums = {0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1};
    int k = 3;

    Solution sol;
    int answer = sol.run(nums, k);

    std::cout << answer << std::endl;
}