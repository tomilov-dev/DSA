#include <vector>
#include <iostream>
#include <algorithm>
#include <climits>
using std::vector;

class Solution
{
public:
    int run(vector<int> &prices)
    {
        int maxprice = 0;

        for (int i = 0; i < prices.size(); i++)
        {
            for (int j = i + 1; j < prices.size(); j++)
            {
                maxprice = std::max(maxprice, prices[j] - prices[i]);
            }
        }

        return maxprice;
    }

    int run2(vector<int> &prices)
    {
        int minprice = INT_MAX;
        int maxprofit = 0;

        for (int price : prices)
        {
            minprice = std::min(minprice, price);
            int profit = price - minprice;
            maxprofit = std::max(maxprofit, profit);
        }

        return maxprofit;
    }
};

int main()
{

    vector<int> prices = {7, 1, 5, 3, 6, 4};

    Solution sol;
    int answer = sol.run2(prices);

    std::cout << answer << std::endl;
}