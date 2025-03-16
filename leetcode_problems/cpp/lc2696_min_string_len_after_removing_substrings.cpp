#include <string>
#include <stack>
using std::stack;
using std::string;

class Solution
{
public:
    int minLength(string s)
    {
        stack<char> st;
        for (char chr : s)
        {
            if (!st.empty() && chr == 'B' && st.top() == 'A')
            {
                st.pop();
            }
            else if (!st.empty() && chr == 'D' && st.top() == 'C')
            {
                st.pop();
            }
            else
            {
                st.push(chr);
            }
        }
        return st.size();
    }
};