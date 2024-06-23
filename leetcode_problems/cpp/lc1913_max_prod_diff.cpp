#include <vector>
#include <iostream>
#include <climits>
using std::vector;

class Solution
{
public:
    int run(vector<int> &nums)
    {
        int a, b = 0;
        int c, d = INT_MAX;
        for (int num : nums)
        {
            if (num > a)
            {
                b = a;
                a = num;
            }
            else if (num > b)
            {
                b = num;
            }

            if (num < c)
            {
                d = c;
                c = num;
            }
            else if (num < d)
            {
                d = num;
            }
        }

        return (a * b) - (c * d);
    }
};

int main()
{
    vector<int> nums = {5,
                        6,
                        2,
                        7,
                        4};

    Solution sol;
    int answer = sol.run(nums);

    std::cout << answer << std::endl;
}