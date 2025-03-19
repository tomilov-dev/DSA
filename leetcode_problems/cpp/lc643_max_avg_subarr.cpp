#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
#include <climits>
using std::vector;

class Solution
{
public:
    double run(vector<int> &nums, int k)
    {
        double sum = 0, max_avg = INT_MIN;
        for (int index = 0; index < k; index++)
        {
            sum += nums[index];
        }

        for (int index = k; index < nums.size(); index++)
        {
            max_avg = std::max(max_avg, sum);
            sum += -nums[index - k] + nums[index];
        }
        max_avg = std::max(max_avg, sum) / k;
        return max_avg;
    }
};

class Solution2
{
public:
    double findMaxAverage(vector<int> &nums, int k)
    {
        double sum = 0;
        double max = 0;
        for (int i = 0; i < k && i < nums.size(); i++)
        {
            sum += nums[i];
        }
        max = sum / k;
        for (int i = k; i < nums.size(); i++)
        {
            sum -= nums[i - k];
            sum += nums[i];
            max = std::max(max, sum / k);
        }
        return max;
    }
};

int main()
{
    vector<int> nums = {1, 12, -5, -6, 50, 3};
    int k = 4;

    Solution sol;

    double answer = sol.run(nums, k);

    std::cout << answer << std::endl;
    return 0;
}