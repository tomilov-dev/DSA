#include <vector>
#include <iostream>
#include <unordered_map>
#include <limits>
#include <algorithm>
using std::unordered_map;
using std::vector;

class Solution
{
public:
    bool isGood(vector<int> &nums)
    {
        unordered_map<int, int> map;
        int maxv = std::numeric_limits<int>::min();
        int minv = std::numeric_limits<int>::max();
        for (int &num : nums)
        {
            map[num]++;
            maxv = std::max(maxv, num);
            minv = std::min(minv, num);
        }
        if (minv != 1 || map[maxv] != 2)
        {
            return false;
        }
        for (int index = 1; index < maxv; index++)
        {
            if (map[index] != 1)
            {
                return false;
            }
        }
        return true;
    }
};

int main()
{
    vector<int> nums = {1, 3, 3, 2};
    Solution sol;
    std::cout << sol.isGood(nums) << std::endl;
    return 0;
}