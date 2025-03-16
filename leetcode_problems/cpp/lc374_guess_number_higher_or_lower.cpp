int guess(int num)
{
    return 0;
}

class Solution
{
public:
    int guessNumber(int n)
    {
        int low = 0;
        int high = n;
        while (high - low > 1)
        {
            int mid = low + (high - low) / 2;
            int guessed = guess(mid);
            if (guessed == 0)
            {
                return mid;
            }
            else if (guessed == 1)
            {
                low = mid;
            }
            else // means -1 => higher
            {
                high = mid;
            }
        }
        return high;
    }
};