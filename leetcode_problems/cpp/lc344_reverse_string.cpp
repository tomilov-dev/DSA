#include <vector>
using std::vector;

class Solution {
public:
    void reverseString(vector<char>& s) {
        int p1 = 0;
        int p2 = s.size() - 1;
        while (p1 < p2) {
            char temp = s[p1];
            s[p1] = s[p2];
            s[p2] = temp;
            p1 ++;
            p2 --;
        }
    }
};

int main() {
    vector<char> s;
    Solution sol;
    sol.reverseString(s);
    return 0;
}