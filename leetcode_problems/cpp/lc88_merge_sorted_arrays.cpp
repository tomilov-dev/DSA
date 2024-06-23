#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    void run(vector<int> &nums1, int m,
             vector<int> &nums2, int n)
    {
        int p1 = m - 1;
        int p2 = n - 1;
        int p3 = m + n - 1;

        while (p2 >= 0)
        {
            if (p1 >= 0 && nums1[p1] > nums2[p2])
            {
                nums1[p3] = nums1[p1];
                p1--;
            }
            else
            {
                nums1[p3] = nums2[p2];
                p2--;
            }
            p3--;
        }
    }
};

int main()
{
    vector<int> nums1 = {1, 3, 7, 0, 0, 0};
    vector<int> nums2 = {2, 5, 8};

    Solution sol;
    sol.run(nums1, 3, nums2, nums2.size());

    for (int num : nums1)
    {
        std::cout << num << std::endl;
    }
}