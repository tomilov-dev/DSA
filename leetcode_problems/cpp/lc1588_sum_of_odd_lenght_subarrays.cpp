#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    int sumOddLengthSubarrays(vector<int> &arr)
    {
        int n = arr.size();
        int sum = 0;
        for (int i = 0; i < n; i++)
        {
            for (int len = 1; i + len <= n; len += 2)
            {
                for (int j = i; j < i + len; j++)
                {
                    sum += arr[j];
                }
            }
        }
        return sum;
    }

    int sumOddLengthSubarraysPrefixSum(vector<int> &arr)
    {
        int n = arr.size();
        int sum = 0;
        vector<int> prefix(n + 1, 0);

        for (int i = 1; i <= n; i++)
        {
            prefix[i] = prefix[i - 1] + arr[i - 1];
        }

        for (int i = 0; i < n; i++)
        {
            for (int len = 1; i + len <= n; len += 2)
            {
                sum += prefix[i + len] - prefix[i];
            }
        }

        return sum;
    }

    int sumOddLengthSubarraysSolutionN(vector<int> &arr)
    {
        int n = arr.size();
        int sum = 0;

        for (int i = 0; i < n; i++)
        {
            int total = (i + 1) * (n - i);
            int odd = (total + 1) / 2;
            sum += odd * arr[i];
        }

        return sum;
    }
};

int main()
{
    vector<int> arr = {1, 4, 2, 5, 3};
    Solution sol;
    auto res = sol.sumOddLengthSubarraysPrefixSum(arr);
    std::cout << res << std::endl;
    return 0;
}
