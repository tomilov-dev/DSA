class Solution
{
public:
    bool is_good(long long mid, long long n)
    {
        long long sum = mid * (mid + 1) / 2;
        return sum <= n;
    }

    int arrangeCoins(int n)
    {
        long long low = 0;
        long long high = n + 1;
        while (high - low > 1)
        {
            long long mid = low + (high - low) / 2;
            if (is_good(mid, n))
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