#include <vector>
#include <iostream>
#include <unordered_map>
using std::vector, std::unordered_map;

class Solution
{
public:
    int run(vector<int> &nums)
    {
        unordered_map<int, int> map;
        int p1 = 0;
        int p2 = 0;

        while (p1 < nums.size())
        {
            if (map.find(nums[p1]) == map.end())
            {
                map[nums[p1]]++;
                nums[p2++] = nums[p1];
            }
            else
            {
                if (map[nums[p1]] < 2)
                {
                    nums[p2++] = nums[p1];
                    map[nums[p1]]++;
                }
            }
            p1++;
        }
        return p2;
    }
};

int main()
{
    vector<int> nums = {1, 1, 1, 2, 2, 3};

    Solution sol;
    int answer = sol.run(nums);

    // std::cout << answer << std::endl;
    for (int num : nums)
    {
        std::cout << num << std::endl;
    }
}