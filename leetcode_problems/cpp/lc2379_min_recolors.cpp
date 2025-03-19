#include <string>
#include <algorithm>
using std::string;

class Solution
{
public:
    int minimumRecolors(string blocks, int k)
    {
        int n = blocks.size();
        int w = 0;
        int min = 0;
        for (int i = 0; i < k && i < n; i++)
        {
            w += blocks[i] == 'W';
        }
        min = w;
        for (int i = k; i < n; i++)
        {
            w -= blocks[i - k] == 'W';
            w += blocks[i] == 'W';
            min = std::min(min, w);
        }
        return min;
    }
};