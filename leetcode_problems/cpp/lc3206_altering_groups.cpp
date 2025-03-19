#include <vector>
using std::vector;

class Solution
{
public:
    int numberOfAlternatingGroups(vector<int> &colors)
    {
        int n = colors.size();
        int count = 0;
        for (int i = 0; i < n; i++)
        {
            int j = (i + 1) % n;
            int k = (i + 2) % n;
            count += colors[i] != colors[j] && colors[j] != colors[k];
        }
        return count;
    }
};
