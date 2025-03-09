#include <algorithm>
#include <iostream>

class Solution
{
public:
    int digit_sum(int n)
    {
        int sum = 0;
        while (n > 0)
        {
            sum += n % 10;
            n /= 10;
        }
        return sum;
    }

    int countLargestGroup(int n)
    {
        int arr[50] = {};
        int maxv = 0;
        for (int i = 1; i <= n; i++)
        {
            int ds = digit_sum(i);
            arr[ds]++;
            maxv = std::max(maxv, arr[ds]);
        }

        int res = 0;
        for (int i = 0; i < 50; i++)
        {
            if (arr[i] == maxv)
            {
                res++;
            }
        }
        return res;
    }
};

int main()
{
    Solution sol;
    std::cout << sol.countLargestGroup(10) << std::endl;
    return 0;
}