#include <vector>
#include <stack>
#include <algorithm>
using std::stack;
using std::vector;

class Solution
{
public:
    vector<int> finalPrices(vector<int> &prices)
    {
        stack<int> st;
        vector<int> res(prices.size());
        for (int i = prices.size() - 1; i >= 0; i--)
        {
            int price = prices[i];
            while (!st.empty() && st.top() > price)
            {
                st.pop();
            }
            if (!st.empty())
            {
                res[i] = price - st.top();
            }
            else
            {
                res[i] = price;
            }
            st.push(price);
        }
        return res;
    }
};
