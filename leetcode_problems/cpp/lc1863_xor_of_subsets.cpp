#include <vector>
using std::vector;

class Solution
{
public:
    void backtrack(vector<int> &nums, int i, int xr, int &sum)
    {
        sum += xr;
        for (int j = i; j < nums.size(); j++)
        {
            xr ^= nums[j];
            backtrack(nums, j + 1, xr, sum);
            xr ^= nums[j];
        }
    }

    int subsetXORSum(vector<int> &nums)
    {
        int sum = 0;
        int xr = 0;
        backtrack(nums, 0, xr, sum);
        return sum;
    }
};
