#include <vector>
#include <string>
#include <stack>
using std::stack;
using std::string;
using std::vector;

class Solution
{
public:
    int calPoints(vector<string> &operations)
    {
        stack<int> st;
        for (string op : operations)
        {
            if (op == "+")
            {
                int t1 = st.top();
                st.pop();
                int t2 = st.top();
                st.push(t1);
                st.push(t1 + t2);
            }
            else if (op == "D")
            {
                st.push(st.top() * 2);
            }
            else if (op == "C")
            {
                st.pop();
            }
            else
            {
                st.push(std::stoi(op));
            }
        }

        int sum = 0;
        while (!st.empty())
        {
            sum += st.top();
            st.pop();
        }
        return sum;
    }
};