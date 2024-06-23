#include <string>
#include <iostream>
#include <algorithm>

class Solution
{
public:
    int run(std::string str)
    {
        int maxlen = 0;
        int chars[256] = {0};
        int p1 = 0;
        int p2 = 0;

        while (p2 < str.length())
        {
            chars[str[p2]]++;

            while (chars[str[p2]] > 1)
            {
                chars[str[p1]]--;
                p1++;
            }

            maxlen = std::max(maxlen, p2 - p1 + 1);
            p2++;
        }

        return maxlen;
    }
};

int main()
{
    std::string str = "pwwkew";

    Solution sol;
    int answer = sol.run(str);

    std::cout << answer << std::endl;

    return 0;
}