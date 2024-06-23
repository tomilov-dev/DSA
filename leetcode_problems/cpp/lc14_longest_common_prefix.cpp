#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <climits>
using std::sort, std::string, std::vector, std::min;

class Solution
{
public:
    string run(vector<string> strings)
    {
        string prefix("");
        sort(strings.begin(), strings.end());
        int size = strings.size() - 1;
        int minlen = min(strings[0].size(), strings[size].size());

        for (int index = 0; index < minlen; index++)
        {
            if (strings[0][index] == strings[size][index])
            {
                prefix += strings[0][index];
            }
            else
            {
                break;
            }
        }
        return prefix;
    }
};

int main()
{
    vector<string> strings = {"flower",
                              "flow",
                              "flight"};

    Solution sol;
    string answer = sol.run(strings);

    std::cout << answer << std::endl;
}