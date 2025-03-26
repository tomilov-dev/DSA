#include <vector>
#include <queue>
using std::priority_queue;
using std::vector;

class Solution
{
public:
    int lastStoneWeight(vector<int> &stones)
    {
        priority_queue<int> heap;
        for (int st : stones)
        {
            heap.push(st);
        }
        while (heap.size() > 1)
        {
            int f = heap.top();
            heap.pop();
            int s = heap.top();
            heap.pop();
            if (s != f)
            {
                heap.push(f - s);
            }
        }
        return heap.size() > 0 ? heap.top() : 0;
    }
};
