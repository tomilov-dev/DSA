#include <iostream>
#include <vector>
using std::vector;

class Solution
{
public:
    vector<int> mostVisited(int n, vector<int> &rounds)
    {
        vector<int> arr(n, 0);
        for (int i = 1; i < rounds.size(); i++)
        {
            int start = rounds[i - 1];
            int end = rounds[i];
            if (start <= end)
            {
                for (int j = start; j < end; j++)
                {
                    arr[j - 1]++;
                }
            }
            else
            {
                for (int j = start; j <= n; j++)
                {
                    arr[j - 1]++;
                }
                for (int j = 1; j < end; j++)
                {
                    arr[j - 1]++;
                }
            }
        }
        arr[rounds.back() - 1]++;

        int xmax = 0;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] > xmax)
            {
                xmax = arr[i];
            }
        }

        vector<int> res;
        for (int i = 0; i < n; i++)
        {
            if (arr[i] == xmax)
            {
                res.push_back(i + 1);
            }
        }
        return res;
    }

    vector<int> mostVisited2(int n, vector<int> &rounds)
    {
        const int start = rounds[0];
        const int end = rounds[rounds.size() - 1];
        vector<int> res;
        if (start <= end)
        {
            for (int i = start; i <= end; i++)
            {
                res.push_back(i);
            }
        }
        else
        {
            for (int i = 1; i <= end; i++)
            {
                res.push_back(i);
            }
            for (int i = start; i <= n; i++)
            {
                res.push_back(i);
            }
        }
        return res;
    }
};

int main()
{
    vector<int> rounds = {1, 3, 1, 2};
    int n = 4;
    Solution sol;
    auto res = sol.mostVisited(n, rounds);
    for (int i = 0; i < res.size(); i++)
    {
        std::cout << res[i] << std::endl;
    }
    return 0;
}
