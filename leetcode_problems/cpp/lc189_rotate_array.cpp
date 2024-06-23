#include <vector>
#include <iostream>
#include <algorithm>
using std::vector, std::reverse;

class Solution
{
public:
    void run(vector<int> &nums, int k)
    {
        int n = nums.size();
        vector<int> extra;

        for (int num : nums)
        {
            extra.push_back(num);
        }

        for (int index = 0; index < n; index++)
        {
            nums[(index + k) % n] = extra[index];
        }
    }

    void run2(vector<int> &nums, int k)
    {
        int n = nums.size();
        k = k % n;

        reverse(nums.begin(), nums.begin() + n - k);
        reverse(nums.begin() + n - k, nums.begin() + n);
        reverse(nums.begin(), nums.begin() + n);
    }
};

int main()
{
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    int k = 3;

    Solution sol;
    sol.run2(nums, k);

    for (int num : nums)
    {
        std::cout << num << std::endl;
    }
}
