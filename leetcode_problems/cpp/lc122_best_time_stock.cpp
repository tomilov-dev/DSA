#include <vector>
#include <iostream>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int run(vector<int> &prices)
    {
        int maxprofit = 0;
        int index = 0;
        int buy, sell;
        int n = prices.size() - 1;

        while (index < n)
        {
            while (index < n && prices[index] >= prices[index + 1])
            {
                index++;
            }
            buy = prices[index];

            while (index < n && prices[index + 1] > prices[index])
            {
                index++;
            }
            sell = prices[index];

            maxprofit += sell - buy;
        }

        return maxprofit;
    }

    int run2(vector<int> &prices)
    {
        int maxprofit = 0;
        for (int index = 1;
             index < prices.size();
             index++)
        {
            maxprofit += std::max(prices[index] - prices[index - 1], 0);
        }

        return maxprofit;
    }
};

int main()
{
    vector<int> prices = {1, 3, 7, 3, 6, 9};

    Solution sol;
    int answer = sol.run2(prices);

    std::cout << answer << std::endl;
}