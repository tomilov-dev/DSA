#include <string>
#include <iostream>
#include <algorithm>
#include <cctype>
using std::string, std::tolower, std::isalnum;

class Solution
{
public:
    bool run(string str)
    {
        int p1 = 0;
        int p2 = str.size() - 1;

        while (p1 < p2)
        {
            while (p1 < p2 && !isalnum(str[p1]))
            {
                p1++;
            }
            while (p1 < p2 && !isalnum(str[p2]))
            {
                p2--;
            }

            if (tolower(str[p1++]) != tolower(str[p2--]))
            {
                return false;
            }
        }

        return true;
    }
};

int main()
{
    string str = "A man, a plan, a canal: Panama";

    Solution sol;
    bool answer = sol.run(str);

    std::cout << answer << std::endl;
}