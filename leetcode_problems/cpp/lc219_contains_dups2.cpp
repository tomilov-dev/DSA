#include <vector>
#include <iostream>
#include <unordered_map>
using std::vector, std::unordered_map;

class Solution
{
public:
    bool run(vector<int> &nums, int k)
    {
        unordered_map<int, vector<int>> map;
        for (int i = 0; i < nums.size(); i++)
        {
            map[nums[i]].push_back(i);
        }

        for (auto it : map)
        {
            std::vector<int> ixs = it.second;
            for (int i = 0; i < ixs.size() - 1; i++)
            {
                if (abs(ixs[i] - ixs[i + 1]) <= k)
                {
                    return true;
                }
            }
        }

        return false;
    }

    bool run2(vector<int> &nums, int k)
    {
        if (nums.size() <= 1)
        {
            return false;
        }

        unordered_map<int, int> map;

        int p1 = 0;
        int p2 = 0;

        while (p1 < nums.size() - k)
        {
            while (p2 < p1 + k)
            {
                p2++;
                if (nums[p1] == nums[p2])
                {
                    return true;
                }
                else
                {
                    map[p2]++;
                }
            }
            p1++;
        }

        return false;
    }
};

int main()
{
    vector<int> nums = {1, 2, 3, 1};
    int k = 3;

    Solution sol;
    bool answer = sol.run2(nums, k);

    std::cout << answer << std::endl;
}