#include <vector>
#include <cmath>
#include <unordered_map>
using std::pow;
using std::unordered_map;
using std::vector;

class Solution
{
public:
    bool is_valid(int cur, int prev)
    {
        int xr = cur ^ prev;
        return xr > 0 && (xr & (xr - 1)) == 0;
    }

    bool backtrack(int i, int k, vector<int> &stack, bool *used, unordered_map<int, vector<int>> &nb)
    {
        if (i >= k)
        {
            return is_valid(stack[0], stack[stack.size() - 1]);
        }

        for (int j : nb[stack[i - 1]])
        {
            if (used[j] || !is_valid(j, stack[i - 1]))
            {
                continue;
            }

            used[j] = true;
            stack[i] = j;
            if (backtrack(i + 1, k, stack, used, nb))
            {
                return true;
            }
            stack[i] = -1;
            used[j] = false;
        }

        return false;
    }

    vector<int> gen_neighbors(int num, int n)
    {
        vector<int> nb;
        for (int i = 0; i < n; i++)
        {
            nb.push_back(num ^ (1 << i));
        }
        return nb;
    }

    vector<int> circularPermutation(int n, int start)
    {
        int k = pow(2, n);
        bool *used = new bool[k];
        for (int i = 0; i < k; i++)
        {
            used[i] = false;
        }
        used[start] = true;

        vector<int> stack(k);
        for (int i = 0; i < stack.size(); i++)
        {
            stack[i] = -1;
        }
        stack[0] = start;

        unordered_map<int, vector<int>> nb;
        for (int i = 0; i < k; i++)
        {
            nb[i] = gen_neighbors(i, n);
        }

        backtrack(1, k, stack, used, nb);
        delete[] used;
        return stack;
    }
};
