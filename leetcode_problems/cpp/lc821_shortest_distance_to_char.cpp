#include <vector>
#include <string>
#include <limits>
#include <algorithm>
using std::numeric_limits;
using std::string;
using std::vector;

class Solution
{
public:
    vector<int> shortestToChar(string s, char c)
    {
        int n = s.size();
        vector<int> res(n, numeric_limits<int>::max());

        int prev = -1;
        for (int i = 0; i < n; i++)
        {
            if (s[i] == c)
            {
                prev = i;
            }
            if (prev != -1)
            {
                res[i] = i - prev;
            }
        }

        prev = -1;
        for (int i = n - 1; i >= 0; i--)
        {
            if (s[i] == c)
            {
                prev = i;
            }
            if (prev != -1)
            {
                res[i] = std::min(res[i], prev - i);
            }
        }

        return res;
    }
};

int main()
{
    return 0;
}