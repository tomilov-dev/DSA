#include <string>
#include <stack>
#include <algorithm>
using std::stack;
using std::string;

class Solution
{
public:
    string reversePrefix(string word, char ch)
    {
        size_t pos = word.find(ch);
        if (pos != string::npos)
        {
            std::reverse(word.begin(), word.begin() + pos + 1);
        }
        return word;
    }
};