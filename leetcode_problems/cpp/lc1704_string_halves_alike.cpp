#include <string>
#include <iostream>
#include <unordered_set>
using std::string, std::unordered_set;

class Solution
{
public:
    unordered_set<char> vowels{'a', 'e', 'i', 'o', 'u',
                               'A', 'E', 'I', 'O', 'U'};

    int count(string str, int start, int end)
    {
        int counter = 0;
        for (int index = start; index < end; index++)
        {
            char chr = str[index];
            if (vowels.find(chr) != vowels.end())
            {
                counter++;
            }
        }
        return counter;
    }

    bool run(string str)
    {
        int mid = str.length() / 2;
        int c1 = count(str, 0, mid);
        int c2 = count(str, mid, str.length());

        return c1 == c2;
    }
};

int main()
{
    string str = "aaabbb";

    Solution sol;
    auto answer = sol.run(str);

    std::cout << answer << std::endl;
}