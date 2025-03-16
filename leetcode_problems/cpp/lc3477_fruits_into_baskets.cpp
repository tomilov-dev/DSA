#include <vector>
#include <iostream>
#include <algorithm>
using std::vector;

class Solution
{
public:
    int numOfUnplacedFruits(vector<int> &fruits, vector<int> &baskets)
    {
        int n = fruits.size();
        int res = 0;
        vector<bool> placed(n, false);
        for (int i = 0; i < n; i++)
        {
            bool done = false;
            int fruit = fruits[i];
            for (int j = 0; j < n; j++)
            {
                if (placed[j])
                {
                    continue;
                }
                int backet = baskets[j];
                if (fruit <= backet)
                {
                    placed[j] = true;
                    done = true;
                    break;
                }
            }
            if (!done)
            {
                res++;
            }
        }
        return res;
    }
};

int main()
{
    vector<int> fruits = {4, 2, 5};
    vector<int> baskets = {3, 5, 4};
    Solution sol;
    int res = sol.numOfUnplacedFruits(fruits, baskets);
    std::cout << res << std::endl;
    return 0;
}
