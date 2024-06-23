#include <string>
#include <iostream>
using std::string;

class Solution
{
public:
    int run(string str)
    {
        int len = 0;
        int index = str.length() - 1;

        while (index >= 0 && str[index] == ' ')
        {
            index--;
        }

        while (index >= 0 && str[index] != ' ')
        {
            len++;
            index--;
        }

        return len;
    }
};

int main()
{
    // string str = "Hello World";
    string str = "a";

    Solution sol;
    auto answer = sol.run(str);

    std::cout << answer << std::endl;
}