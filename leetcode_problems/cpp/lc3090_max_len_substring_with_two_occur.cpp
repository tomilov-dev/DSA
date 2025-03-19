#include <string>
#include <algorithm>
using std::string;

class Solution
{
public:
    int maximumLengthSubstring(string s)
    {
        int map[26];
        map[s[0] - 'a']++;
        map[s[1] - 'a']++;
        int max = 2;
        int p1 = 0;
        for (int p2 = 2; p2 < s.size(); p2++)
        {
            map[s[p2] - 'a']++;
            while (p1 < s.size() && map[s[p2] - 'a'] > 2)
            {
                map[s[p1] - 'a']--;
                p1++;
            }
            max = std::max(max, p2 - p1 + 1);
        }
        return max;
    }
};
