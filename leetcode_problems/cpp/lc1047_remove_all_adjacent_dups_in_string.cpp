#include <string>
#include <stack>
#include <algorithm>
using std::stack;
using std::string;

class Solution
{
public:
    string removeDuplicates(string s)
    {
        stack<char> st;
        for (char chr : s)
        {
            if (!st.empty() && chr == st.top())
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
            res += st.top();
            st.pop();
        }
        std::reverse(res.begin(), res.end());
        return res;
    }
};

class SolutionString
{
public:
    string removeDuplicates(string s)
    {
        string res;
        for (char chr : s)
        {
            if (!res.empty() && chr == res.back())
            {
                res.pop_back();
            }
            else
            {
                res.push_back(chr);
            }
        }
        return res;
    }
};

class SolutionInplace
{
public:
    string removeDuplicates(string s)
    {
        int n = s.size();
        int i = 0;
        for (int j = 0; j < n; ++j)
        {
            if (i > 0 && s[i - 1] == s[j])
            {
                --i;
            }
            else
            {
                s[i] = s[j];
                ++i;
            }
        }
        return s.substr(0, i);
    }
};

int main()
{
    return 0;
}