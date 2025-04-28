#include <vector>
#include <cmath>
using std::vector;

class Solution
{
public:
    int coinChange(vector<int> &coins, int amount)
    {
        int n = amount + 1;
        vector<int> dp(n, std::pow(10, 5));
        dp[0] = 0;
        for (int coin : coins)
        {
            for (int i = coin; i < n; i++)
            {
                dp[i] = std::min(dp[i], dp[i - coin] + 1);
            }
        }
        return dp[amount] == std::pow(10, 5) ? -1 : dp[amount];
    }
};