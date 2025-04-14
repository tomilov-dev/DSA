#include <string>
using std::string;

class Solution
{
public:
    bool backtrack(string &stack, int &count, int n, int k)
    {
        if (stack.size() >= n)
        {
            count++;
            return count == k;
        }

        for (char chr : std::string("abc"))
        {
            if (!stack.empty() && stack.back() == chr)
            {
                continue;
            }
            stack.push_back(chr);
            if (backtrack(stack, count, n, k))
            {
                return true;
            }
            stack.pop_back();
        }
        return false;
    }

    string getHappyString(int n, int k)
    {
        int count = 0;
        string stack = "";
        if (backtrack(stack, count, n, k))
        {
            return stack;
        }
        return "";
    }
};