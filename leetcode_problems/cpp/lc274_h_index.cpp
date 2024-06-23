#include <vector>
#include <iostream>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int run(vector<int> &citations)
    {
        if (citations.size() == 1)
        {
            if (citations[0] == 0)
            {
                return 0;
            }
            else
            {
                return 1;
            }
        }

        std::sort(citations.begin(), citations.end());

        int index = 0;
        int h_index = 0;

        int cur_int = 0;
        int maxlen = citations.size();
        int maxint = citations[maxlen - 1];

        while (cur_int <= maxint)
        {
            int count = maxlen - index;
            if (cur_int <= count)
            {
                h_index = cur_int;
            }
            else
            {
                break;
            }

            while (cur_int == citations[index] && index < maxlen - 1)
            {
                index++;
            }

            cur_int++;
        }

        return h_index;
    }
};

int main()
{
    vector<int> citations = {0, 0};

    Solution sol;
    auto answer = sol.run(citations);

    std::cout << answer << std::endl;
}