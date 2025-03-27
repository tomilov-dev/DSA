#include <vector>
#include <queue>
#include <algorithm>
using std::priority_queue;
using std::vector;

class Solution
{
public:
    int minimumOperations(vector<int> &nums)
    {
        int res = 0;
        priority_queue<int> heap;

        for (int num : nums)
        {
            if (num > 0)
            {
                heap.push(-num);
            }
        }

        while (!heap.empty())
        {
            int smallest = -heap.top();
            heap.pop();

            while (!heap.empty() && -heap.top() == smallest)
            {
                heap.pop();
            }

            res++;
        }

        return res;
    }
};
