#include <string>
#include <algorithm>
using std::string;

class Solution
{
public:
    string makeGood(string s)
    {
        string res;
        for (char chr : s)
        {
            if (res.size() == 0)
            {
                res.push_back(chr);
                continue;
            }

            char prev = res[res.size() - 1];
            if (prev != chr && std::tolower(prev) == std::tolower(chr))
            {
                res.pop_back();
            }
            else
            {
                res.push_back(chr);
            }
        }
        return res;
    }
};