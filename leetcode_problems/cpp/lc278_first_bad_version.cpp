bool isBadVersion(int version)
{
    return true;
}

class Solution
{
public:
    int firstBadVersion(int n)
    {
        int low = 0;
        int high = n;
        while (high - low > 1)
        {
            int mid = low + (high - low) / 2;
            if (isBadVersion(mid))
            {
                high = mid;
            }
            else
            {
                low = mid;
            }
        }
        return high;
    }
};