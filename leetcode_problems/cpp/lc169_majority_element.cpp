#include <vector>
#include <iostream>
#include <unordered_map>
using std::vector, std::unordered_map;

class Solution
{
public:
    int run(vector<int> &nums)
    {
        int major;
        int appears = 0;
        unordered_map<int, int> map;

        for (int num : nums)
        {
            map[num]++;
        }

        for (auto pt : map)
        {
            if (pt.second > appears)
            {
                major = pt.first;
                appears = pt.second;
            }
        }

        return major;
    }

    int run2(vector<int> &nums)
    {
        int major;
        int count = 0;
        for (int index = 0;
             index < nums.size();
             index++)
        {
            if (count == 0)
            {
                major = nums[index];
                count++;
            }
            else
            {
                if (major == nums[index])
                {
                    count++;
                }
                else
                {
                    count--;
                }
            }
        }

        return major;
    }
};

int main()
{
    vector<int> nums = {3, 2, 3};

    Solution sol;
    int answer = sol.run2(nums);

    std::cout << answer << std::endl;
}