#include <vector>
#include <iostream>
#include <unordered_map>
#include <unordered_set>
using std::unordered_map;
using std::unordered_set;
using std::vector;

class Solution
{
public:
    vector<int> findIntersectionValues(vector<int> &nums1, vector<int> &nums2)
    {
        unordered_map<int, int> m1;
        unordered_map<int, int> m2;
        for (int &num : nums1)
        {
            m1[num]++;
        }
        for (int &num : nums2)
        {
            m2[num]++;
        }
        int r1 = 0;
        int r2 = 0;
        for (auto &pair : m1)
        {
            int k = pair.first;
            int v = pair.second;
            if (m2[k] > 0)
            {
                r1 += v;
            }
        }
        for (auto &pair : m2)
        {
            int k = pair.first;
            int v = pair.second;
            if (m1[k] > 0)
            {
                r2 += v;
            }
        }
        return {r1, r2};
    }
};

int main()
{
    return 0;
}