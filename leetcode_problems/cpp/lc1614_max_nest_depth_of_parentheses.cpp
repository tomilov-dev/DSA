#include <string>
#include <stack>
#include <algorithm>
using std::stack;
using std::string;

class Solution
{
public:
    int maxDepth(string s)
    {
        int max = 0;
        stack<char> st;
        for (char chr : s)
        {
            if (chr == '(')
            {
                st.push(chr);
                max = std::max(max, static_cast<int>(st.size()));
            }
            else if (chr == ')')
            {
                st.pop();
            }
        }
        return max;
    }
};