#include <vector>
using std::vector;

class Solution
{
public:
    bool large(vector<int> seqA, vector<int> seqB)
    {
        if (seqA.size() > seqB.size())
        {
            return true;
        }
        else if (seqA.size() < seqB.size())
        {
            return false;
        }
        else
        {
            for (int i = 0; i < seqA.size(); i++)
            {
                if (seqA[i] == seqB[i])
                {
                    continue;
                }
                return seqA[i] > seqB[i];
            }
            return false;
        }
    }

    void backtrack(
        int i,
        int n,
        vector<bool> &nums,
        vector<int> &stack,
        vector<int> &res,
        bool &found)
    {
        if (found)
        {
            return;
        }

        if (i >= stack.size())
        {
            if (large(stack, res))
            {
                res = stack;
                found = true;
            }
            return;
        }

        if (stack[i] != -1)
        {
            backtrack(i + 1, n, nums, stack, res, found);
            return;
        }

        for (int num = n; num > 0; num--)
        {
            if (!nums[num])
            {
                continue;
            }

            int dist = num == 1 ? 0 : num;
            if (i + dist >= stack.size() || stack[i + dist] != -1)
            {
                continue;
            }

            stack[i] = num;
            stack[i + dist] = num;
            nums[num] = false;

            backtrack(i + 1, n, nums, stack, res, found);

            stack[i] = -1;
            stack[i + dist] = -1;
            nums[num] = true;
        }
    }

    vector<int> constructDistancedSequence(int n)
    {
        bool found = false;
        vector<bool> nums(n + 1, true);
        vector<int> stack(1 + (n - 1) * 2, -1);
        vector<int> res;
        backtrack(0, n, nums, stack, res, found);
        return res;
    }
};