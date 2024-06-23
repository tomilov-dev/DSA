#include <unordered_map>
#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    int run(vector<int> &nums, int k)
    {
        int k_count = 0;
        std::unordered_map<int, int> mapper = {};

        for (int num : nums)
        {
            mapper[num]++;
        }

        int num_count = 0;
        int other_num = 0;
        int other_num_count = 0;
        for (int num : nums)
        {
            other_num = k - num;
            mapper[num]--;
            mapper[other_num]--;
            if (mapper[num] >= 0 && mapper[other_num] >= 0)
            {
                k_count++;
            }
            else
            {
                mapper[num]++;
                mapper[other_num]++;
            }
        }

        return k_count;
    }
};

int main()
{
    vector<int> nums = {3, 1, 3, 4, 3};
    int k = 5;

    Solution sol;

    int answer = sol.run(nums, k);

    std::cout << answer << std::endl;
}