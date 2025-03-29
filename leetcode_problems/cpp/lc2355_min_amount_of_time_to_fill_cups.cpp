#include <vector>
#include <queue>
using std::vector;
using std::priority_queue;

class Solution {
public:
    int fillCups(vector<int>& amount) {
        priority_queue<int> heap;
        int res = 0;
        for (int num: amount) {
            if (num > 0) {
                heap.push(num);
            }
        }
        while (!heap.empty()) {
            if (heap.size() > 1) {
                int f = heap.top() - 1;
                heap.pop();
                int s = heap.top() - 1;
                heap.pop();
                if (f > 0) {
                    heap.push(f);
                }
                if (s > 0) {
                    heap.push(s);
                }
            } else {
                int f = heap.top() - 1;
                heap.pop();
                if (f > 0) {
                    heap.push(f);
                }
            }
            res++;
        }
        return res;
    }
};
