#include <cmath>
#include <vector>
#include <queue>
using std::priority_queue;
using std::vector>

class Solution {
public:
    long long pickGifts(vector<int>& gifts, int k) {
        priority_queue<int> heap;
        for (int g : gifts) {
            heap.push(g);
        }
        while (k && !heap.empty()) {
            int g = heap.top();
            heap.pop();
            g = static_cast<int>(std::floor(std::sqrt(g)));
            if (g > 0) {
                heap.push(g);
            }
            k--;
        }
        long long sum = 0;
        while (!heap.empty()) {
            sum += heap.top();
            heap.pop();
        }
        return sum;
    }
};
