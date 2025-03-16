#include <vector>
#include <string>
#include <stack>
using std::stack;
using std::string;
using std::vector;

class Solution
{
public:
    int minOperations(vector<string> &logs)
    {
        stack<string> st;
        for (const string &log : logs)
        {
            if (log == "../")
            {
                if (!st.empty())
                {
                    st.pop();
                }
            }
            else if (log == "./")
            {
                continue;
            }
            else
            {
                st.push(log);
            }
        }
        return st.size();
    }
};