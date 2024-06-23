#include <string>
#include <iostream>
#include <unordered_map>
using std::string, std::unordered_map;

class Solution
{
public:
    int run(string &str)
    {
        unordered_map<string, int> mapper = {
            {"I", 1},
            {"V", 5},
            {"X", 10},
            {"L", 50},
            {"C", 100},
            {"D", 500},
            {"M", 1000},
        };

        int number = 0;
        int previous_number = 0;

        for (int index = str.size() - 1; index >= 0; index--)
        {
            int curnum = mapper[str.substr(index, 1)];
            if (curnum >= previous_number)
            {
                number += curnum;
            }
            else
            {
                number -= curnum;
            }
            previous_number = curnum;
        }

        return number;
    }
};

int main()
{
    string roman = "III";

    Solution sol;
    auto answer = sol.run(roman);

    std::cout << answer << std::endl;

    return 0;
}