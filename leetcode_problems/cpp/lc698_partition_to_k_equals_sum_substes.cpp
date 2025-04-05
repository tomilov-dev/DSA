#include <vector>
#include <algorithm>
using std::vector;

class Solution
{
public:
    bool backtrack(int i, int t, vector<int> &nums, int subs[], int k)
    {
        if (i >= nums.size())
        {
            for (int isub = 0; isub < k; isub++)
            {
                if (subs[isub] != t)
                {
                    return false;
                }
            }
            return true;
        }

        for (int isub = 0; isub < k; isub++)
        {
            if (subs[isub] + nums[i] <= t)
            {
                subs[isub] += nums[i];
                if (backtrack(i + 1, t, nums, subs, k))
                {
                    return true;
                }
                subs[isub] -= nums[i];
            }

            if (subs[isub] == 0)
            {
                break;
            }
        }
        return false;
    }

    bool canPartitionKSubsets(vector<int> &nums, int k)
    {
        int n = nums.size();
        long long nsum = 0;
        for (int num : nums)
        {
            nsum += num;
        }
        if (nsum <= 0 || nsum % k != 0)
        {
            return false;
        }

        int t = nsum / k;
        if (*std::max_element(nums.begin(), nums.end()) > t)
        {
            return false;
        }

        std::sort(nums.rbegin(), nums.rend());
        int *subs = new int[n]();
        return backtrack(0, t, nums, subs, k);
    }
};