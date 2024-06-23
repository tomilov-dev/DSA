#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    int run(vector<int> &nums, int val)
    {
        int k = nums.size();
        int p1 = 0;
        int p2 = 0;
        while (p1 < nums.size())
        {
            if (nums[p1] == val)
            {
                k--;
            }
            else
            {
                nums[p2++] = nums[p1];
            }
            p1++;
        }
        return k;
    }
};

int main()
{
    vector<int> nums = {3, 2, 2, 3};
    int val = 3;

    Solution sol;
    int answer = sol.run(nums, val);

    std::cout << answer << std::endl;
}