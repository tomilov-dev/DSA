#include <vector>
#include <iostream>
using std::vector;

class Soltion
{
public:
    int run(vector<int> &nums)
    {
        int p1 = 1;
        int p2 = 0;

        while (p1 < nums.size())
        {
            if (nums[p1] != nums[p2])
            {
                nums[++p2] = nums[p1];
            }
            p1++;
        }
        return p2 + 1;
    }
};

int main()
{
    vector<int> nums = {1, 1, 2};

    Soltion sol;
    int answer = sol.run(nums);

    // std::cout << answer << std::endl;
    for (int num : nums)
    {
        std::cout << num << std::endl;
    }
}