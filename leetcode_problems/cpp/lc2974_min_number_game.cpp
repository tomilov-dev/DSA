#include <vector>
#include <queue>
using std::vector;
using std::priority_queue;

class Solution {
public:
    vector<int> numberGame(vector<int>& nums) {
        priority_queue<int> heap;
        vector<int> res;
        for (int num: nums) {
            heap.push(-num);
        }
        while (!heap.empty()) {
            int f = heap.top();
            heap.pop();
            int s = heap.top();
            heap.pop();
            res.push_back(-s);
            res.push_back(-f);
        }
        return res;
    }
};
