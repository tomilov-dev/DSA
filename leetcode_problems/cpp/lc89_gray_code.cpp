#include <vector>
#include <iostream>
#include <unordered_set>
using std::unordered_set;
using std::vector;

class Solution
{
public:
    bool backtrack(int n, vector<int> &res, unordered_set<int> &visited)
    {
        if (res.size() == (1 << n))
        {
            return true;
        }

        int last = res.back();
        for (int i = 0; i < n; i++)
        {
            int next = last ^ (1 << i);
            if (visited.count(next) == 0)
            {
                res.push_back(next);
                visited.insert(next);
                if (backtrack(n, res, visited))
                {
                    return true;
                }

                res.pop_back();
                visited.erase(next);
            }
        }
        return false;
    }

    vector<int> grayCode(int n)
    {
        vector<int> res = {0};
        unordered_set<int> visited = {0};
        backtrack(n, res, visited);
        return res;
    }
};

int main()
{
    int n = 2;
    Solution sol;
    vector<int> res = sol.grayCode(n);
    for (int num : res)
    {
        std::cout << num << std::endl;
    }
}
