#include <string>
#include <iostream>
using std::string;

class Solution
{
public:
    bool run(string string1, string string2)
    {
        if (string1.size() == 0)
        {
            return true;
        }

        int pointer = 0;
        for (auto chr : string2)
        {
            if (string1.at(pointer) == chr)
            {
                pointer++;
            }

            if (pointer == string1.size())
            {
                return true;
            }
        }

        return false;
    }
};

int main()
{
    string string1 = "abc";
    string string2 = "ahbgdc";

    Solution sol;
    bool answer = sol.run(string1, string2);

    std::cout << answer << std::endl;

    return 0;
}