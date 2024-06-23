#include <vector>
#include <climits>
#include <iostream>
using std::vector;

class Solution
{
public:
    bool run(vector<int> nums)
    {
        int v1 = INT_MAX;
        int v2 = INT_MAX;

        for (int num : nums)
        {
            if (num <= v1)
            {
                v1 = num;
            }
            else if (num <= v2)
            {
                v2 = num;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
};

int main()
{
    vector<int> nums = {2,
                        1,
                        5,
                        0,
                        4,
                        6};

    Solution sol;
    bool answer = sol.run(nums);
    std::cout << answer << std::endl;

    return 0;
}