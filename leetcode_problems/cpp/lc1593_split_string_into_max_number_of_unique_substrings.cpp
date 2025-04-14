#include <string>
#include <unordered_set>
#include <algorithm>
using std::string;
using std::unordered_set;

class Solution
{
public:
    int backtrack(int i, int n, string &s, unordered_set<string> &uniq)
    {
        if (i >= s.size())
        {
            return uniq.size();
        }

        int max = 0;
        for (int j = i + 1; j < n + 1; j++)
        {
            string sub = s.substr(i, j - i);
            if (!uniq.count(sub))
            {
                uniq.insert(sub);
                int imax = backtrack(j, n, s, uniq);
                max = std::max(max, imax);
                uniq.erase(sub);
            }
        }
        return max;
    }

    int maxUniqueSplit(string s)
    {
        int n = s.size();
        unordered_set<string> uniq;
        return backtrack(0, n, s, uniq);
    }
};
