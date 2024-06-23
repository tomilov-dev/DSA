#include <vector>
#include <string>
#include <iostream>
using std::string, std::vector;

class Solution
{
public:
    string run(string str)
    {
        string new_str = "";

        for (int index = 0; index < str.length(); index++)
        {
            char chr = str[index];
            if (chr == '*')
            {
                new_str.pop_back();
            }
            else
            {
                new_str.push_back(str[index]);
            }
        }

        return new_str;
    }

    string run2(string str)
    {
        int pointer = 0;
        for (int index = 0; index < str.length(); index++)
        {
            if (str[index] == '*')
            {
                pointer--;
            }
            else
            {
                str[pointer++] = str[index];
            }
        }

        return str.substr(0, pointer);
    }
};

int main()
{
    string str = "leet**cod*e";

    Solution sol;
    auto answer = sol.run(str);
    std::cout << answer << std::endl;
}