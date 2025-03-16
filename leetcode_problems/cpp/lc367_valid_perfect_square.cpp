class Solution
{
public:
    bool is_good(long value, long target)
    {
        return (value * value) <= target;
    }

    bool isPerfectSquare(long num)
    {
        long low = 0;
        long high = num + 1;
        while (high - low > 1)
        {
            long mid = low + (high - low) / 2;
            if (is_good(mid, num))
            {
                low = mid;
            }
            else
            {
                high = mid;
            }
        }
        return low * low == num;
    }
};