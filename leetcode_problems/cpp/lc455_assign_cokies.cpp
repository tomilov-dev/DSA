#include <vector>
#include <algorithm>
using std::vector;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
        sort(g.begin(), g.end());
        sort(s.begin(), s.end());
        int p1 = 0;
        int p2 = 0;
        int res = 0;
        while (p1 < g.size() && p2 < s.size()) {
            if (g[p1] <= s[p2]) {
                res++;
                p1++;
                p2++;
            } else {
                p2++;
            }
        }
        return res;
    }
};

int main() {
    vector<int> g = {1, 2, 3};
    vector<int> s = {1, 1};
    Solution sol;
    int result = sol.findContentChildren(g, s);
    std::cout << "Number of content children: " << result << std::endl;
    return 0;
}