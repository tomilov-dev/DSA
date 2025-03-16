#include <string>
#include <stack>
using std::stack;
using std::string;

class Solution
{
public:
    stack<char> to_stack(string s)
    {
        stack<char> st;
        for (char chr : s)
        {
            if (chr == '#')
            {
                if (!st.empty())
                {
                    st.pop();
                }
            }
            else
            {
                st.push(chr);
            }
        }
        return st;
    }

    bool backspaceCompare(string s, string t)
    {
        stack<char> st1 = to_stack(s);
        stack<char> st2 = to_stack(t);
        if (st1.size() != st2.size())
        {
            return false;
        }
        while (!st1.empty())
        {
            if (st1.top() != st2.top())
            {
                return false;
            }
            st1.pop();
            st2.pop();
        }
        return true;
    }
};