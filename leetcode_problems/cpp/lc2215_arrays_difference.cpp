#include <vector>
#include <iostream>
#include <unordered_set>
#include <set>
#include <algorithm>
#include <iterator>
using std::vector;

class Solution
{
public:
    vector<vector<int>> run(vector<int> &nums1, vector<int> &nums2)
    {
        vector<vector<int>> diff = {{}, {}};
        std::unordered_set<int> uniqs1;
        std::unordered_set<int> uniqs2;

        int index = 0;
        while (index < nums1.size() || index < nums2.size())
        {
            if (index < nums1.size())
            {
                uniqs1.insert(nums1[index]);
            }
            if (index < nums2.size())
            {
                uniqs2.insert(nums2[index]);
            }
            index++;
        }

        int di1, di2 = 0;
        for (auto num1 : uniqs1)
        {
            if (uniqs2.find(num1) == uniqs2.end())
            {
                diff[0].push_back(num1);
                di1++;
            }
        }

        for (auto num2 : uniqs2)
        {
            if (uniqs1.find(num2) == uniqs1.end())
            {
                diff[1].push_back(num2);
                di2++;
            }
        }

        return diff;
    }

    vector<vector<int>> run2(vector<int> &nums1, vector<int> &nums2)
    {
        vector<int> v1, v2;
        std::set<int> s1(std::begin(nums1), std::end(nums1)), s2(std::begin(nums2), std::end(nums2));
        std::set_difference(std::begin(s1), std::end(s1),
                            std::begin(s2), std::end(s2), back_inserter(v1));
        std::set_difference(std::begin(s2), std::end(s2),
                            std::begin(s1), std::end(s1), back_inserter(v2));
        return {v1, v2};
    }
};

int main()
{
    vector<int> nums1 = {1, 2, 3};
    vector<int> nums2 = {2, 4, 6};

    Solution sol;
    auto answer = sol.run2(nums1, nums2);

    for (auto num : answer[1])
    {
        std::cout << num << std::endl;
    }
}