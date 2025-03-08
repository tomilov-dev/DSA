#include <vector>
#include <iostream>
using std::vector;

class Solution
{
public:
    vector<vector<int>> construct2DArray(vector<int> &original, int m, int n)
    {
        if (m * n != original.size())
        {
            vector<vector<int>> res;
            return res;
        }

        vector<vector<int>> res;
        int index = 0;
        for (int i = 0; i < m; i++)
        {
            vector<int> sub = {};
            for (int j = 0; j < n; j++)
            {
                sub.push_back(original[index]);
                index++;
            }
            res.push_back(sub);
        }
        return res;
    }
};

class Solution
{
public:
    vector<vector<int>> construct2DArray(vector<int> &original, int m, int n)
    {
        if (m * n != original.size())
        {
            return {};
        }

        vector<vector<int>> res(m, vector<int>(n));
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                res[i][j] = original[i * n + j];
            }
        }
        return res;
    }
};

int main()
{
    vector<int> original = {1, 2, 3, 4};
    int m = 2;
    int n = 2;
    Solution sol;
    auto res = sol.construct2DArray(original, m, n);
    return 0;
}