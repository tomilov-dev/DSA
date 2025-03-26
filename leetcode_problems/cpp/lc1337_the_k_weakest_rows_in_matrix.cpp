#include <vector>
#include <algorithm>
#include <queue>
using std::priority_queue;
using std::vector;

class Solution
{
public:
    vector<int> kWeakestRows(vector<vector<int>> &mat, int k)
    {
        int n = mat.size();
        int m = mat[0].size();
        vector<int> result = {};
        priority_queue<std::pair<int, int>> heap;
        for (int i = 0; i < n; i++)
        {
            int sum = 0;
            for (int el : mat[i])
            {
                sum += el;
            }
            heap.push(std::pair(-sum, -i));
        }
        while (result.size() < k)
        {
            result.push_back(-heap.top().second);
            heap.pop();
        }
        return result;
    }
};

class SolutionWithoutMinus
{
public:
    vector<int> kWeakestRows(vector<vector<int>> &mat, int k)
    {
        int n = mat.size();
        priority_queue<std::pair<int, int>> heap;

        for (int i = 0; i < n; i++)
        {
            int sum = 0;
            for (int el : mat[i])
            {
                sum += el;
            }
            heap.push(std::make_pair(sum, i));
            if (heap.size() > k)
            {
                heap.pop();
            }
        }

        vector<int> result;
        while (!heap.empty())
        {
            result.push_back(heap.top().second);
            heap.pop();
        }

        std::reverse(result.begin(), result.end());
        return result;
    }
};