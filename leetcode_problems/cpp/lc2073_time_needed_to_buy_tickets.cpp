#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    int timeRequiredToBuy(vector<int> &tickets, int k)
    {
        int res = 0;
        int target = tickets[k];
        for (int i = 0; i < tickets.size(); i++)
        {
            if (i <= k)
            {
                res += std::min(target, tickets[i]);
            }
            else
            {
                res += std::min(target - 1, tickets[i]);
            }
        }
        return res;
    }
};

int main()
{
    vector<int> tickets = {5, 1, 1, 1};
    int k = 0;
    Solution sol;
    int res = sol.timeRequiredToBuy(tickets, k);
    std::cout << res << std::endl;
    return 0;
}