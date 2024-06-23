#include <iostream>
#include <vector>
#include <string>
using std::vector, std::string;

class Solution
{
public:
    int run(vector<char> &chars)
    {
        int walker = 0;
        for (int runner = 1, count = 1; runner <= chars.size(); runner++, count++)
        {
            if (runner == chars.size() || chars[runner] != chars[runner - 1])
            {
                chars[walker++] = chars[runner - 1];
                if (count >= 2)
                    for (char digit : std::to_string(count))
                        chars[walker++] = digit;
                count = 0;
            }
        }
        return walker;
    }
};

int main()
{
    vector<char> chars = {'a', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'};

    Solution sol;
    int answer = sol.run(chars);

    std::cout << answer << std::endl;
    return 0;
}