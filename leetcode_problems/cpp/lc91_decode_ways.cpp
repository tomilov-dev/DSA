#include <string>
#include <iostream>
#include <unordered_set>

class Solution
{
public:
    int memo[100] = {};
    int run(const std::string &s)
    {
        return dp(s, 0);
    }

    int dp(const std::string &s, int i)
    {
        if (i == s.size())
            return 1;
        if (memo[i] != 0)
            return memo[i];
        int ans = 0;
        if (s[i] != '0') // Single digit
            ans += dp(s, i + 1);
        if (i + 1 < s.size() && (s[i] == '1' || s[i] == '2' && s[i + 1] <= '6')) // Two digits
            ans += dp(s, i + 2);
        return memo[i] = ans;
    }
};

int main()
{
    std::string str = "12206";

    Solution sol;
    int answer = sol.run(str);

    std::cout << answer << std::endl;
}