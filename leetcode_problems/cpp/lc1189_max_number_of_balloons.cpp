#include <unordered_map>
#include <string>
#include <iostream>
#include <limits>
using std::string;
using std::unordered_map;

class Solution
{
public:
    int maxNumberOfBalloons(string text)
    {
        unordered_map<char, int> word = {
            {'b', 1},
            {'a', 1},
            {'l', 2},
            {'o', 2},
            {'n', 1}};
        unordered_map<char, int> char_count;
        for (char c : text)
        {
            char_count[c]++;
        }

        int min_count = std::numeric_limits<int>::max();
        for (const auto &pair : word)
        {
            char target_char = pair.first;
            int target_count = pair.second;
            min_count = std::min(min_count, char_count[target_char] / target_count);
        }

        return min_count;
    }
};

int main()
{
    string text = "nlaebolko";
    Solution sol;
    auto res = sol.maxNumberOfBalloons(text);
    std::cout << res << std::endl;
    return 0;
}