#include <string>
#include <iostream>
#include <unordered_map>
#include <algorithm>
using std::string;

class Solution
{
    int vowels[26] = {1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1};

public:
    int run(string str, int k)
    {
        std::unordered_map<char, int> mapper;
        mapper['a']++, mapper['e']++, mapper['i']++;
        mapper['o']++, mapper['u']++;

        int max_vow = 0;
        int cur_vow = 0;
        for (int index = 0; index < str.length(); index++)
        {
            cur_vow += mapper[str[index]];
            if (index >= k)
            {
                cur_vow -= mapper[str[index - k]];
            }
            max_vow = std::max(max_vow, cur_vow);
        }
        return max_vow;
    }

    int run2(string str, int k)
    {
        int max_vow = 0;
        for (auto i = 0, cur_vow = 0; i < str.size(); ++i)
        {
            cur_vow += vowels[str[i] - 'a'];
            if (i >= k)
                cur_vow -= vowels[str[i - k] - 'a'];
            max_vow = std::max(max_vow, cur_vow);
        }
        return max_vow;
    }
};

int main()
{
    string str = "leetcode";
    int k = 3;

    Solution sol;
    int answer = sol.run(str, k);

    std::cout << answer << std::endl;
}