#include <string>
#include <iostream>
using std::string;

class Solution
{
public:
    int run(string haystack, string needle)
    {
        if (haystack.length() < needle.length())
        {
            return -1;
        }
        if (haystack.length() == needle.length())
        {
            if (haystack == needle)
            {
                return 0;
            }
            else
            {
                return -1;
            }
        }

        for (int index = 0;
             index <= haystack.length() - needle.length();
             index++)
        {
            int point = 0;
            for (; point < needle.length(); point++)
            {
                if (haystack[index + point] != needle[point])
                {
                    break;
                }
            }

            if (point == needle.length())
            {
                return index;
            }
        }

        return -1;
    }
};

int main()
{
    string haystack = "aaa";
    string needle = "aaaa";

    Solution sol;
    int answer = sol.run(haystack, needle);

    std::cout << answer << std::endl;
}