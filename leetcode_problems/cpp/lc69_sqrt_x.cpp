#include <iostream>

class Solution
{
public:
    bool is_good(long value, long target)
    {
        return (value * value) <= target;
    }

    int mySqrt(long x)
    {
        long low = 0;
        long high = x + 1;
        while (high - low > 1)
        {
            long mid = low + (high - low) / 2;
            if (is_good(mid, x))
            {
                low = mid;
            }
            else
            {
                high = mid;
            }
        }
        return low;
    }
};

int main()
{
    int x = 4;
    Solution sol;
    int res = sol.mySqrt(x);
    std::cout << res << std::endl;
    return 0;
}
