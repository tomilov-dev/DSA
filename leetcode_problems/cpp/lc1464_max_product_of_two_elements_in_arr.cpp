#include <vector>
#include <queue>
using std::priority_queue;
using std::vector;

class Solution
{
public:
    int maxProduct(vector<int> &nums)
    {
        priority_queue<int> heap;
        for (int num : nums)
        {
            heap.push(num);
        }
        int f = heap.top();
        heap.pop();
        int s = heap.top();
        return (f - 1) * (s - 1);
    }
};