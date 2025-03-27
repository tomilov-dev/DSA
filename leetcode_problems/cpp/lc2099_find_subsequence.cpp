#include <vector>
#include <queue>
#include <algorithm>
using std::pair;
using std::priority_queue;
using std::vector;

class Solution
{
public:
    vector<int> maxSubsequence(vector<int> &nums, int k)
    {
        int n = nums.size();
        priority_queue<pair<int, int>> heap;

        for (int i = 0; i < n; i++)
        {
            heap.push(pair(-nums[i], i));
            if (heap.size() > k)
            {
                heap.pop();
            }
        }

        vector<pair<int, int>> resultHeap;
        while (!heap.empty())
        {
            pair<int, int> el = heap.top();
            heap.pop();
            resultHeap.push_back({-el.first, el.second});
        }

        std::sort(resultHeap.begin(), resultHeap.end(), [](pair<int, int> &a, pair<int, int> &b)
                  { return a.second < b.second; });

        vector<int> res;
        for (auto &p : resultHeap)
        {
            res.push_back(p.first);
        }

        return res;
    }
};
