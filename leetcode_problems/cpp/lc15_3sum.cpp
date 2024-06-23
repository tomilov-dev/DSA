#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <string>
using std::vector, std::unordered_map, std::string;

class Solution
{
public:
    vector<vector<int>> run1(vector<int> &nums)
    {
        vector<vector<int>> res;
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < nums.size(); i++)
        {

            int target = -nums[i];
            int p1 = i + 1;
            int p2 = nums.size() - 1;

            while (p1 < p2)
            {
                int sum = nums[p1] + nums[p2];
                if (sum < target)
                    p1++;
                else if (sum > target)
                    p2--;
                else
                {
                    vector<int> triplet = {nums[i], nums[p1], nums[p2]};
                    res.push_back(triplet);

                    while (p1 < p2 && nums[p1] == triplet[1])
                        p1++;
                    while (p1 < p2 && nums[p2] == triplet[2])
                        p2--;
                }
            }

            while (i + 1 < nums.size() && nums[i + 1] == nums[i])
                i++;
        }
        return res;
    }
};

int main()
{
    // vector<int> nums = {-4, -3, -2, -1, 0, 1, 2, 3, 4};
    // vector<int> nums = {0, 0, 0};
    vector<int> nums = {-1, 0, 1, 2, -1, -4};

    Solution sol;
    auto answer = sol.run1(nums);

    for (auto sub : answer)
    {
        std::cout << "{";
        for (int num : sub)
        {
            std::cout << num << ",";
        }
        std::cout << "}" << std::endl;
    }
}