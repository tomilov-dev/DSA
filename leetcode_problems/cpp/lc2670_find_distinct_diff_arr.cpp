#include <vector>
#include <iostream>
#include <unordered_map>
using std::unordered_map;
using std::vector;

class Solution
{
public:
    vector<int> distinctDifferenceArray(vector<int> &nums)
    {
        int prefdist = 0;
        int suffdist = 0;
        vector<int> diff;
        unordered_map<int, int> prefmap;
        unordered_map<int, int> suffmap;

        for (int num : nums)
        {
            if (prefmap[num] == 0)
            {
                prefdist++;
            }
            prefmap[num]++;
        }

        for (int num : nums)
        {
            prefmap[num]--;
            if (suffmap[num] == 0)
            {
                suffdist++;
            }
            suffmap[num]++;
            if (prefmap[num] == 0)
            {
                prefdist--;
            }
            diff.push_back(suffdist - prefdist);
        }

        return diff;
    }
};

int main()
{
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5};
    vector<int> result = sol.distinctDifferenceArray(nums);
    for (int val : result)
    {
        std::cout << val << " ";
    }
    std::cout << std::endl;
    return 0;
}