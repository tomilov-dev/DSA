#include <vector>
using std::vector;

class Solution
{
public:
    bool is_good(char value, char target)
    {
        return (value - 'a') <= (target - 'a');
    }

    char nextGreatestLetter(vector<char> &letters, char target)
    {
        int low = -1;
        int high = letters.size();
        while (high - low > 1)
        {
            int mid = low + (high - low) / 2;
            if (is_good(letters[mid], target))
            {
                low = mid;
            }
            else
            {
                high = mid;
            }
        }
        return high == letters.size() ? letters[0] : letters[high];
    }
};