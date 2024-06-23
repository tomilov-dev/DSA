#include <unordered_map>
#include <string>
#include <stack>
#include <iostream>
using std::string, std::stack, std::unordered_map;

class Solution
{
public:
    bool run(string str)
    {
        if (str.size() % 2 == 0)
        {
            unordered_map<char, char> mapper = {{'(', ')'}, {'{', '}'}, {'[', ']'}};
            stack<char> stack;

            for (auto chr : str)
            {
                if (mapper.find(chr) != mapper.end())
                {
                    stack.push(chr);
                }
                else if (stack.empty() || mapper.at(stack.top()) != chr)
                {
                    return false;
                }
                else
                {
                    stack.pop();
                }
            }
            return stack.empty();
        }
        return false;
    }
};

int main()
{
    string str = "()[]{}";
    Solution sol;

    bool answer = sol.run(str);

    std::cout << answer << std::endl;
}