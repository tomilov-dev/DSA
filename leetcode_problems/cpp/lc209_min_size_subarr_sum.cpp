#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using std::vector;

class Solution
{
public:
    int run(int target, vector<int> &nums)
    {
        int p1 = 0;
        int p2 = 0;
        int sum = 0;
        int minimum = INT_MAX;
        bool found = false;

        while (p1 < nums.size() && p2 < nums.size())
        {
            sum += nums[p2++];
            while (p1 < nums.size() && sum >= target)
            {
                minimum = std::min(minimum, p2 - p1);
                found = true;
                sum -= nums[p1++];
            }
        }

        minimum = found ? minimum : 0;
        return minimum;
    }
};

int main()
{
    // int target = 4;
    // vector<int> nums = {1, 4, 4};

    int target = 11;
    vector<int> nums = {1, 2, 3, 4, 5};

    // int target = 7;
    // vector<int> nums = {2, 3, 1, 2, 4, 3};

    Solution sol;
    int answer = sol.run(target, nums);

    std::cout << answer << std::endl;
}