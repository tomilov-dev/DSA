#include <string>
#include <stack>
#include <cctype>
#include <algorithm>
using std::stack;
using std::string;

class Solution
{
public:
    string clearDigits(string s)
    {
        stack<char> st;
        for (char chr : s)
        {
            if (!st.empty() && std::isdigit(chr))
            {
                st.pop();
            }
            else
            {
                st.push(chr);
            }
        }

        string res;
        while (!st.empty())
        {
            res.push_back(st.top());
            st.pop();
        }

        std::reverse(res.begin(), res.end());
        return res;
    }
};